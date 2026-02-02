# Prompt History - Challenge 1

1.  Let's begin with challenge 1. Start by creating a file challenge1.py

    I would like you to generate python code for an email validation function that uses regex functions to validates email addresses by handling common edge cases (plus addressing, subdomains).

    **Generated Code:**
    ```python
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
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
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
    ```

2.  The previous regex failed the test case `user@.com.my` (it was valid but should be invalid due to the leading dot). Please update the regex to ensure that the domain part does not start with a dot or hyphen, but still handles subdomains correctly.

    **Generated Code:**
    ```python
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$'
    ```
