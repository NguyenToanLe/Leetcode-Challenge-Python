# 4. Climbing Stairs
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2`. In how many distinct ways can you climb to the top?

**Example 1**:
```
Input:        n = 2
Output:       2
Explaination: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2**:
```
Input:        n = 3
Output:       3
Explaination: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**
- `1 <= n <= 45`


## Solution Explanation
The task can be re-written as find the arrangement of 2 to put in the steps (permutation without order).

Then just increase the number of 2s until we reach `n`, calculate arrangement and accumulate to the final result.
