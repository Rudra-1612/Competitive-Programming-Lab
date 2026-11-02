# 8 DSA Programs in Python

Beginner-friendly implementations of the eight problems from the assignment.

## Requirements
- Python 3.9 or newer
- No third-party packages are required

## Run each program
Open a terminal in this folder and run:

```bash
python 01_xor_swap.py
python 02_single_number.py
python 03_remove_duplicates_hash_set.py
python 04_binary_search_descending.py
python 05_two_sum_hash_map.py
python 06_valid_parentheses_stack.py
python 07_fibonacci_tabulation.py
python 08_activity_selection.py
```

## Run all tests

```bash
python -m unittest -v
```

## Logic and complexity

| # | Program | Core idea | Time | Extra space |
|---|---|---|---|---|
| 1 | XOR Swap | Three XOR operations exchange values; XOR cancels equal bits | O(1) | O(1) |
| 2 | Single Number | XOR is associative/commutative and `x ^ x = 0`, `x ^ 0 = x` | O(n) | O(1) |
| 3 | Remove Duplicates | A set remembers seen values; append only the first occurrence | O(n) average | O(n) |
| 4 | Descending Binary Search | Compare the middle value and discard half, reversing the usual direction for descending order | O(log n) | O(1) |
| 5 | Two Sum | Store previously seen values; look for `target - current` | O(n) average | O(n) |
| 6 | Valid Parentheses | Stack stores opening brackets; each closing bracket must match the latest opener | O(n) | O(n) |
| 7 | Fibonacci Tabulation | Build answers from F(0), F(1) upward | O(n) | O(n) |
| 8 | Activity Selection | Sort by finish time and repeatedly choose the earliest-finishing compatible activity | O(n log n) | O(n) for sorted copy/output |

## Sample outputs

- XOR Swap: `Before: 10 20` then `After:  20 10`
- Single Number: `Single number: 4`
- Remove Duplicates: `Without duplicates: [4, 2, 1, 3]`
- Descending Binary Search: index `2` for target `60`, and `-1` for `50`
- Two Sum: `Indices: [0, 1]`
- Valid Parentheses: `([]{}) -> True`, `([)]   -> False`
- Fibonacci: `F(7) = 13`
- Activity Selection: `[(1, 3), (4, 6), (6, 7), (8, 9)]`, count `4`

## Important assumptions
- Single Number: exactly one value occurs once and every other value occurs exactly twice.
- Descending Binary Search: input is already sorted in descending order.
- Two Sum: returns the first valid pair encountered, or an empty list if no pair exists.
- Valid Parentheses: input contains only bracket characters.
- Activity Selection: an activity starting exactly when the previous one finishes is considered compatible.

## Oral explanation tip
For every program, explain in this order:
1. What problem is being solved.
2. Which data structure or algorithm is used.
3. How one sample input moves through the code.
4. Time and extra-space complexity.
