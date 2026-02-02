# Challenge 1: Email Validation Analysis

## Prompt Iteration Process

### Version 1 (Baseline)
**Prompt**: "Generate python code for an email validation function that uses regex functions to validates email addresses by handling common edge cases (plus addressing, subdomains)."
**Result**: Failed one test case (`user@.com.my`) - Validated an invalid email.
**Issues**: The regex `[a-zA-Z0-9.-]+` for the domain part allowed it to start with a dot, which is invalid.

**Test Snapshot (v1 Failure)**:
```text
Email: user@.com.my | Expected: False | Actual: True | Result: FAIL
```

### Version 2 (Refined)
**Prompt**: "The previous regex failed the test case `user@.com.my` (it was valid but should be invalid due to the leading dot). Please update the regex to ensure that the domain part does not start with a dot or hyphen, but still handles subdomains correctly."
**Result**: Passed all test cases.
**Changes**: The regex was updated to explicitely require the domain segment to start with an alphanumeric character: `@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?`.

## Comparison

| Feature | Version 1 | Version 2 |
| :--- | :--- | :--- |
| **Correctness** | 8/9 Pass | 9/9 Pass |
| **Complexity** | Simple regex, easier to read. | More complex regex using non-capturing groups `(?:...)` to enforce structure. |
| **Robustness** | Weak against invalid domain formats. | Stronger validation of domain structure (start/end chars). |

## Conclusion
The v2 prompt specifically targeted the structural flaw in the domain validation logic. By asking for a restriction on the starting character of the domain, the LLM generated a more rigorous pattern that enforces standard hostname rules (RFC 1035 style).
