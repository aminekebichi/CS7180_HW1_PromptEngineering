# Prompt Engineering Challenges

## Objective
The goal of this project is to master effective prompting techniques through rigorous iteration and experimentation. By systematically refining prompts and analyzing the results, we aim to understand what drives high-quality code generation from LLMs.

## Challenges
This project consists of 3 distinct coding challenges designed to test and improve prompting skills.

### Challenge 1: Easy (25%)
**Task**: Email validation function with regex

- Create a function that validates email addresses
- Handle common edge cases (plus addressing, subdomains)
- Include test cases

### Challenge 2: Medium (35%)
**Task**: React sortable/filterable data table with pagination

- Sortable columns (click to sort)
- Filter by text input
- Pagination (configurable page size)
- Proper TypeScript types

### Challenge 3: Hard (40%)
**Task**: Caching layer with TTL, LRU eviction, persistence

- Time-to-live (TTL) for entries
- Least Recently Used (LRU) eviction when full
- Persistence to `localStorage` or file
- Configurable max size

## Workflow
For each challenge, we follow this structured approach:

1.  **Initial Prompt (v1)**: Draft and execute a baseline prompt to solve the challenge.
2.  **Generate & Test**: Run the generated code and verify its functionality.
3.  **Iterate & Improve**: Refine the prompt (v2, v3, etc.) based on the initial results, issues found, or desired optimizations.
4.  **Document**: Record specific changes made to the prompt and *why* they led to better results.
5.  **Compare**: Analyze and compare the quality, efficiency, and correctness of the code across different prompt versions.
