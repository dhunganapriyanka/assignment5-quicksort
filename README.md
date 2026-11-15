# Assignment 5: Quicksort Algorithm

## Overview

This project implements and compares Deterministic Quicksort and Randomized Quicksort using Python. It examines how pivot selection and input distribution affect sorting performance.

## Algorithms

- Deterministic Quicksort uses the last element as the pivot.
- Randomized Quicksort selects a random pivot.

## Running the Program

1. Install Python 3.
2. Open the project folder in VS Code.
3. Run `python quicksort.py` in the terminal.
4. View the performance results in the terminal and the generated `results.csv` file.

## Performance Testing

Both algorithms are tested using random, sorted, and reverse-sorted arrays of 500, 1,000, and 2,000 elements. Execution times are averaged across three trials.

## Findings

Theoretical analysis shows that both versions have O(n log n) average-case performance and O(n²) worst-case performance. Randomization reduces the likelihood of consistently unbalanced partitions.

See the assignment report for experimental results and detailed analysis.
