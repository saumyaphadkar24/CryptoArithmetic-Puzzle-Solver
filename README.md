# Cryptarithmetic Puzzle Solver

## Overview
This Python project implements a solver for cryptarithmetic puzzles using backtracking. In cryptarithmetic puzzles, the digits in a mathematical equation are replaced with letters. Each letter represents a unique digit, and the challenge is to find the digit each letter represents to satisfy the equation.

## Key Functions
- `getCharacters(s)`: Returns a set of all characters in a string.
- `getAllCharacters(s1, s2, ans)`: Returns a list of all unique characters in three input strings.
- `isAssignmentComplete(allVariables, assigned)`: Checks if all variables are assigned.
- `getStartingLetters(s1, s2, ans)`: Returns the starting characters of three input strings.
- `createDomain(s1, s2, ans)`: Creates the domain (possible digits) for each character in the puzzle.
- `generateUpdatedDomain(variable, assignment, s1, s2, ans)`: Updates the domain for a variable based on current assignments.
- `calcMRV(allVariables, assignedCharacters, s1, s2, ans)`: Calculates the Minimum Remaining Values for the unassigned characters.
- `degreeHeuristic(var, s1, s2, ans)`: Applies the degree heuristic to the given variables.
- `selectUnassigned(allVariables, assignedCharacters, s1, s2, ans)`: Selects the next unassigned variable based on MRV and degree heuristic.
- `isValidAssignment(assignment, s1, s2, ans)`: Checks if an assignment of variables is valid and does not cause conflicts.
- `backtrack(assignment, s1, s2, ans)`: Main backtracking function to find a solution to the puzzle.
- `backtracking_search(s1, s2, ans)`: Initiates the backtracking search for a solution.
- `main()`: Main function to read the input, invoke the solver, and write the output.

## Setup and Execution
1. Create an `input.txt` file containing the puzzle in the specified format.
2. Run the script using Python:
`python crypta.py`
3. The solution will be written to `output.txt`.

## File Formats

### Input File Format
The `input.txt` file should contain three lines representing the puzzle:<br>
SEND<br>
MORE<br>
MONEY<br>

Each word represents a part of the cryptarithmetic equation (`WORD1 + WORD2 = RESULT`).

### Output File Format
The `output.txt` file will contain the solution with digits replacing the letters:<br>
9567<br>
1085<br>
10652<br>

## License
This project is licensed under the MIT License.