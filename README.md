# Lab 5: Static Code Analysis

## Objective
This lab focuses on enhancing Python code quality, security, and style by utilizing static analysis tools (Pylint, Bandit, and Flake8) to detect and rectify common programming issues. The goal is to improve code maintainability, security, and adherence to best practices.

## Tools Used
- **Pylint**: A code quality checker that identifies logical errors, unused variables, poor practices, and design flaws.
- **Bandit**: A security linter that detects common security vulnerabilities and insecure coding patterns.
- **Flake8**: A style guide enforcement tool that checks for PEP 8 compliance, including formatting, whitespace, and syntax issues.

## Original Code Issues
The original `inventory_system.py` file contained several issues identified by the static analysis tools:

### Pylint Issues
- Missing module and function docstrings
- Function names not conforming to snake_case (e.g., `addItem` instead of `add_item`)
- Dangerous default value `[]` as argument in `addItem` (mutable default argument)
- Bare `except:` clause without specifying exception types
- Use of `eval()` function (security risk)
- Unused import `logging`
- Missing final newline
- Using `open` without specifying encoding
- Using global statement
- Not using `with` for file operations

### Bandit Issues
- Use of `eval()` (high severity security issue)
- Potential JSON injection via `json.loads()` (though noted as often ignored for simple scripts)

### Flake8 Issues
- PEP 8 style violations, including line length, whitespace, and formatting

## Fixes Applied in `cleaned_inventory_system.py`
The cleaned version addresses at least four key issues, with additional improvements for better code quality:

1. **Mutable Default Argument**: Changed `logs=[]` to `logs=None` and initialized inside the function to avoid shared state across calls.

2. **Bare Except Clause**: Replaced `except:` with `except KeyError:` for specific exception handling in `removeItem`.

3. **Security Risk (eval)**: Removed the dangerous `eval("print('eval used')")` call.

4. **Input Validation**: Added type checking for `item` and `qty` in `addItem` to handle invalid inputs gracefully.

Additional improvements:
- Configured proper logging with `logging.basicConfig()`
- Used f-strings for cleaner string formatting
- Renamed variables to avoid C0103 issues (e.g., `i` to `item_name`)
- Added docstrings and comments for better readability
- Handled potential KeyError in `getQty` by using `.get()` method
- Improved error handling and logging messages
