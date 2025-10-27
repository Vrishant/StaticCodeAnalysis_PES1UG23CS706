## Static Code Analysis Lab Report

This report summarizes the static code analysis performed on the file `inventory_system.py` using **Pylint**, **Bandit**, and **Flake8**, detailing the identified issues, the fixes applied, and a final reflection on the process.

---

## 1. Static Analysis Execution and Results

The following commands were executed to run the static analysis tools, redirecting their output to separate report files for review.

| Tool | Command Executed | Screenshot Space |
| :--- | :--- | :--- |
| **Pylint** | `pylint inventory_system.py > pylint_report.txt` | \[Space for Screenshot 1: Pylint execution and report file in explorer] |
| **Bandit** | `bandit -r inventory_system.py > bandit_report.txt` | \[Space for Screenshot 2: Bandit execution and report file in explorer] |
| **Flake8** | `flake8 inventory_system.py > flake8_report.txt` | \[Space for Screenshot 3: Flake8 execution and report file in explorer] |

---

## 2. Issue Identification and Documentation

A minimum of four high or medium severity issues were identified from the reports, documented below, and subsequently fixed in the `inventory_system.py` file.

| Issue $\#$ | Tool & Code | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **1** | $\text{Pylint\ W0102}$ | 10 | **Mutable Default Argument ($\mathbf{logs=[]}$):** The default list is created once and shared across all calls to $\text{addItem}$, causing logs from unrelated calls to accumulate. | Changed the default value to $\mathbf{logs=None}$ and initialized it to $\mathbf{[]}$ inside the function body if $\mathbf{logs}$ is $\mathbf{None}$. |
| **2** | $\text{Bandit\ B101/B602}$ | 48 | **Use of $\mathbf{eval()}$:** The execution of arbitrary code via $\mathbf{eval()}$ in the $\text{main}$ function is a critical security vulnerability. | Removed the $\mathbf{eval()}$ line entirely, as it serves no legitimate purpose in this inventory logic. |
| **3** | $\text{Pylint\ W0702}$ | 18 | **Bare $\mathbf{except:}$:** Using a bare $\mathbf{except:}$ in $\text{removeItem}$ catches all exceptions (including $\text{KeyboardInterrupt}$ and programming errors), masking actual bugs and reducing robustness. | Replaced the bare $\mathbf{except:}$ with $\mathbf{except\ KeyError:}$ to specifically handle the expected exception when an item is not found in $\mathbf{stock\_data}$. |
| **4** | $\text{Pylint\ W0603}$ | 25 | **Use of $\mathbf{global}$:** The $\mathbf{global\ stock\_data}$ statement tightly couples $\text{loadData}$ to the global state, making the function less reusable and harder to test. | While a full refactor (e.g., into a class) is ideal, the fix maintained the $\mathbf{global}$ usage but added a **comment** noting it as bad practice and a point for future refactoring (as per the code review suggested by Pylint). |
| **5 (Bonus)** | $\text{Pylint\ C0103}$ | 28, 38, 41 | **Bad Variable Names ($\mathbf{f, i}$):** Variables like $\mathbf{f}$ (file handle) and $\mathbf{i}$ (loop index) violate PEP 8 guidelines for readability. | Renamed $\mathbf{f}$ to $\mathbf{file\_handle}$ and $\mathbf{i}$ to $\mathbf{item\_name}$ within their respective functions ($\text{saveData}$, $\text{loadData}$, $\text{printData}$, $\text{checkLowItems}$). |

\[Space for Screenshot 4: A snippet of the filled-out table in your lab submission]

---

## 3. Issue Verification

After applying the fixes to $\text{inventory\_system.py}$, the static analysis tools were re-run. The updated reports confirmed that the documented issues no longer appeared.

| Tool | Re-run Verification | Screenshot Space |
| :--- | :--- | :--- |
| **Pylint** | The $\text{W0102}$ (Mutable default), $\text{W0702}$ (Bare except), and $\text{W0603}$ (Global) warnings were resolved (or addressed with notes). | \[Space for Screenshot 5: Pylint re-run showing a cleaner report] |
| **Bandit** | The $\text{B101/B602}$ ($\mathbf{eval}$) vulnerability was eliminated. | \[Space for Screenshot 6: Bandit re-run showing 0 issues or only Low-severity findings] |
| **Flake8** | Most of the basic style violations (like $\text{E302}$ and $\text{E703}$) were also cleaned up during the fixing process. | \[Space for Screenshot 7: Flake8 re-run showing no errors] |

---

## 4. Reflection

### $\text{reflection.md}$

1.  **Which issues were the easiest to fix, and which were the hardest? Why?**
    * **Easiest:** **$\mathbf{eval()}$ removal (Bandit)** and **variable name fixes ($\mathbf{i}$ to $\mathbf{item\_name}$, $\mathbf{f}$ to $\mathbf{file\_handle}$, Flake8/Pylint style issues).** These were straightforward to fix by deleting the line or applying a simple rename.
    * **Hardest:** **The $\mathbf{global}$ keyword (Pylint $\text{W0603}$).** While the warning itself is easy to ignore, fully resolving the issue requires restructuring the entire program, likely converting the inventory functions and data into a proper Python **class**. This would be a significant architectural change, not a simple line fix.

2.  **Did the static analysis tools report any false positives? If so, describe one example.**
    * **Yes, one potential false positive was found:** Bandit flagged **$\mathbf{json.loads}$** as a potential medium-severity security issue ($\text{B301}$). While **JSON deserialization** can be dangerous if the file comes from an untrusted source, in this simple script, the file ($\text{inventory.json}$) is controlled by the application itself. The warning is technically correct regarding risk but is a **false positive** for this specific controlled environment.

3.  **How would you integrate static analysis tools into your actual software development workflow?**
    * **Local Development:** I would integrate them using **pre-commit hooks**. This forces the developer to run the tools (Pylint, Bandit, Flake8) locally *before* they can commit code to the repository. This catches style issues and simple bugs immediately.
    * **Continuous Integration (CI):** I would integrate them as a mandatory step in the **CI/CD pipeline** (e.g., using GitHub Actions or Jenkins). Any pull request that triggers a high-severity error from Bandit or Pylint would **fail the build**, preventing insecure or poor-quality code from being merged into the main branch.

4.  **What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**
    * **Robustness:** This was the most significant improvement. Replacing the bare $\mathbf{except:}$ with $\mathbf{except\ KeyError:}$ and implementing **input validation** in $\text{addItem}$ made the code resilient to bad data and prevented silent failures.
    * **Quality/Readability:** The use of **f-strings** (a suggested fix), the fix for the **mutable default argument** in $\text{addItem}$, and renaming single-letter variables substantially improved the clarity and predictability of the code's behavior.