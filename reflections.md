# Reflection

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