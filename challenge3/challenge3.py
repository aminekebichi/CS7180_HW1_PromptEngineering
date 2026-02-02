import time
import pickle
import os
import threading
import tempfile
import functools
from collections import OrderedDict

class Cache:
    def __init__(self, max_size=5, ttl=10, persistence_file='cache.pkl'):
        """
        Initialize the cache.
        :param max_size: Maximum number of entries in the cache.
        :param ttl: Time-to-live for entries in seconds.
        :param persistence_file: File path to save/load cache data.
        """
        self.max_size = max_size
        self.ttl = ttl
        self.persistence_file = persistence_file
        self.cache = OrderedDict()
        self.lock = threading.Lock()
        self._load()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._save()

    def get(self, key):
        with self.lock:
            if key not in self.cache:
                return None
            
            entry = self.cache[key]
            if time.time() > entry['expiry']:
                del self.cache[key]
                self._save()
                return None
            
            self.cache.move_to_end(key)
            return entry['value']

    def put(self, key, value):
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            
            self.cache[key] = {
                'value': value,
                'expiry': time.time() + self.ttl
            }
            
            if len(self.cache) > self.max_size:
                self.cache.popitem(last=False)
                
            self._save()
    
    def decorator(self, func):
        """Decorator to cache function results."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create a deterministic key
            # Sort kwargs to ensure {a=1, b=2} is same as {b=2, a=1}
            sorted_kwargs = frozenset(sorted(kwargs.items()))
            key_parts = (func.__name__, args, sorted_kwargs)
            key = str(key_parts)
            
            # Try to get from cache
            val = self.get(key)
            if val is not None:
                return val
            
            # Compute and cache
            result = func(*args, **kwargs)
            self.put(key, result)
            return result
        return wrapper

    def _save(self):
        try:
            dirname = os.path.dirname(self.persistence_file) or '.'
            with tempfile.NamedTemporaryFile(dir=dirname, delete=False, mode='wb') as tf:
                pickle.dump(list(self.cache.items()), tf)
                tempname = tf.name
            os.replace(tempname, self.persistence_file)
        except IOError as e:
            print(f"Error saving cache: {e}")
            if 'tempname' in locals() and os.path.exists(tempname):
                os.remove(tempname)

    def _load(self):
        if not os.path.exists(self.persistence_file):
            return
        try:
            with open(self.persistence_file, 'rb') as f:
                items = pickle.load(f)
                now = time.time()
                for key, entry in items:
                    if entry['expiry'] > now:
                        self.cache[key] = entry
        except (IOError, pickle.PickleError) as e:
            print(f"Error loading cache: {e}")

if __name__ == "__main__":
    print("Running Comprehensive Test Suite for Challenge 3...")
    
    TEST_FILE = 'test_cache_final.pkl'
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

    # Test 1: Pickle Persistence & Atomic Writes
    print("\n[Test 1] Pickle Persistence (Complex Objects)")
    class User:
        def __init__(self, name): self.name = name
        def __repr__(self): return f"User({self.name})"
    
    # Write
    with Cache(max_size=3, ttl=5, persistence_file=TEST_FILE) as cache:
        u1 = User("Alice")
        cache.put("u1", u1)
        print(f"Cached object: {u1}")

    # Reload
    with Cache(max_size=3, ttl=5, persistence_file=TEST_FILE) as cache:
        val = cache.get("u1")
        print(f"Got object from reload: {val} -> {'PASS' if isinstance(val, User) and val.name == 'Alice' else 'FAIL'}")

    # Test 2: LRU Eviction Logic
    print("\n[Test 2] LRU Eviction (Max size 3)")
    with Cache(max_size=3, ttl=5, persistence_file=TEST_FILE) as cache:
        cache.cache.clear()
        # [A]
        cache.put("A", 1) 
        # [A, B]
        cache.put("B", 2) 
        # [A, B, C]
        cache.put("C", 3) 
        
        # Access A -> moves to end (most recent) -> [B, C, A]
        cache.get("A")    
        
        # Put D -> Evict oldest (B) -> [C, A, D]
        cache.put("D", 4) 
        
        val_a = cache.get("A")
        val_b = cache.get("B")
        val_c = cache.get("C")
        
        print(f"Got 'A': {val_a} (Expected: 1) -> {'PASS' if val_a == 1 else 'FAIL'}")
        print(f"Got 'B': {val_b} (Expected: None) -> {'PASS' if val_b is None else 'FAIL'}")
        print(f"Got 'C': {val_c} (Expected: 3) -> {'PASS' if val_c == 3 else 'FAIL'}")

    # Test 3: Decorator
    print("\n[Test 3] Decorator Usage")
    stats = {'call_count': 0}
    
    # New cache instance for decorator test
    dec_cache = Cache(max_size=10, ttl=5)
    
    @dec_cache.decorator
    def expensive_func(x):
        stats['call_count'] += 1
        return x * x
        
    print(f"First call (5): {expensive_func(5)}")
    print(f"Second call (5): {expensive_func(5)}")
    print(f"Call count: {stats['call_count']} (Expected: 1) -> {'PASS' if stats['call_count'] == 1 else 'FAIL'}")
    
    print(f"Third call (6): {expensive_func(6)}")
    print(f"Call count: {stats['call_count']} (Expected: 2) -> {'PASS' if stats['call_count'] == 2 else 'FAIL'}")

    # Cleanup
    if os.path.exists(TEST_FILE):
         os.remove(TEST_FILE)
