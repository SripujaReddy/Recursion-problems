# Recursion in Python
## Overview
This project explores the fundamental programming concept of **recursion** using Python. Recursion is a technique where a function calls itself to solve a smaller instance of the same problem. It is especially useful for problems that can be broken down into similar subproblems.

## What is Recursion?
A function is said to be **recursive** if it calls itself within its definition. Every recursive function must have:
- A **base case** – which stops the recursion
- A **recursive case** – where the function calls itself

### Example:
```python
def factorial(n):
    if n == 0:
        return 1            # Base case
    return n * factorial(n-1)  # Recursive call
