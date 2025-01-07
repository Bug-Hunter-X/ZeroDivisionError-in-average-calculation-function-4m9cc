This repository contains a Python function designed to calculate the average of a list of numbers.  The function includes error handling for empty lists; however, a subtle issue is present.

The `bug.py` file demonstrates the original, flawed function. The `bugSolution.py` demonstrates the corrected function. 

The primary focus is on the uncommon `ZeroDivisionError` that can occur if the input list is empty. Although many handle this via try-except block, a more straightforward and efficient approach is showcased in the solution.