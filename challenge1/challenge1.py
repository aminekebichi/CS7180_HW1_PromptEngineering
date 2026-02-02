import re

def validate_email(email):
    """
    Validates an email address using regex.
    Handles common edge cases like plus addressing and subdomains.
    """
    # Regex pattern explanation:
    # ^[a-zA-Z0-9._%+-]+ : Start with alphanumeric, dots, underscores, %, +, -
    # @                 : Literal @ symbol
    # [a-zA-Z0-9.-]+    : Domain name (alphanumeric, dots, hyphens)
    # \.                : Literal dot
    # [a-zA-Z]{2,}$     : TLD (at least 2 letters)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    return False

if __name__ == "__main__":
    test_cases = [
        ("test@example.com", True),
        ("user.name+tag@example.co.uk", True),
        ("plainaddress", False),
        ("@no-local-part.com", False),
        ("Outlook User <outlook_user@example.com>", False),
        ("user@sub.domain.com", True),
        ("user@domain", False),  # Missing TLD
        ("user@.com.my", False), # Leading dot in domain
        ("user123@123.com", True), # Numeric domain
    ]
    
    print(f"{'Email':<40} | {'Expected':<10} | {'Actual':<10} | {'Result'}")
    print("-" * 75)
    
    for email, expected in test_cases:
        actual = validate_email(email)
        result = "PASS" if actual == expected else "FAIL"
        print(f"{email:<40} | {str(expected):<10} | {str(actual):<10} | {result}")
