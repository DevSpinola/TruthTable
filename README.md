# Logic Gates Truth Table Generator

## Description
This Python script generates the truth table for a given logical expression. It utilizes the `itertools.product` function and a custom `calculate` module.

## How to Use
1. Update the logical expression in the main script.
2. Change the logical expression using only 'AND', 'OR', and 'NOT'. Use only letters to name logic gates.
   
   ```python
   expression = "A and B and C or (not(A and B) and C and D)"
