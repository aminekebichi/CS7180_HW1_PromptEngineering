# Challenge 3: Caching Layer Analysis

## Prompt Iteration Process

### Version 1 (Baseline)
**Prompt**: "Create a caching layer with TTL, LRU eviction, persistence to JSON. Configurable max size."
**Result**: Logic was correct in theory, but the implementation was basic and the test suite had a flawed assumption about LRU (expecting oldest item to persist).
**Analysis**: Good starting point, but not production-ready.

### Version 2 (Robustness)
**Prompt**: "The v1 implementation lacked thread safety and the manual test case for LRU eviction had a logic error. Please refine to be **production-ready**: 1. Thread Safety (Lock). 2. Context Manager (`with` statement). 3. Refined Testing."
**Result**: Passed all tests. Code is now safe for concurrent headers and easier to use (`with` support).
**Analysis**: Significant jump in quality. Addressing both "correctness" (tests) and "reliability" (locks).

### Version 3 (Data Integrity)
**Prompt**: "The JSON persistence limits us to simple data types, and writing to the file directly can cause corruption. Iterate to use **Pickle** (binary) and **Atomic Writes** (temp file -> rename)."
**Result**: Cache can now store arbitrary Python objects (like custom classes) and is resilient to crashes during save.
**Analysis**: Shifted focus to data integrity and flexibility. The code is becoming a robust utility library.

### Version 4 (Developer Experience)
**Prompt**: "Verified. Now focus on **Developer Experience (DX)**. Add a `decorator` method to cache function results automatically."
**Result**: Added `@cache.decorator`.
**Analysis**: The final iteration transforms the explicit usage pattern (`put(key, val)`) into a seamless integration pattern (`@decorator`). This drastically reduces the boilerplate code required to use the cache.

## Comparison

| Feature | v1 (Baseline) | v2 (Robust) | v3 (Integrity) | v4 (DX) |
| :--- | :--- | :--- | :--- | :--- |
| **Logic** | Basic LRU/TTL | + Thread Safe, Context Mgr | + Atomic Writes | + Deterministic Keys |
| **Persistence** | JSON (Simle types) | JSON | Pickle (All types) | Pickle |
| **Usage** | Manual `get/put` | `with cache:` | `with cache:` | `@cache.decorator` |
| **Safety** | Low (Race conditions) | High (Locks) | Very High (Atomic) | Very High |

## Conclusion
By iterating through 4 versions, we evolved a simple homework assignment into a robust, thread-safe, and developer-friendly caching library. Each prompt iteration targeted a specific dimension of software quality: **Correctness -> Reliability -> Integrity -> Usability**.
