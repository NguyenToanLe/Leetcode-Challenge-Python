# 16. Missing Number
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that 
is missing from the array*.

**Example 1**:

```
Input:          nums = [3, 0, 1]
Output:         2
Explanation:    n = 3 since there are 3 numbers, so all numbers are in the range [0, 3]. 2 is the missing number in the 
                range since it does not appear in nums.
```

**Example 2**:

```
Input:          nums = [0, 1]
Output:         2
Explanation:    n = 2 since there are 2 numbers, so all numbers are in the range [0, 2]. 2 is the missing number in the 
                range since it does not appear in nums.
```

**Example 3**:

```
Input:          nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output:         8
Explanation:    n = 9 since there are 9 numbers, so all numbers are in the range [0, 9]. 8 is the missing number in the 
                range since it does not appear in nums.
```


**Constraints:**

- `n == nums.length`
- <code>1 <= n <= 10<sup>4</sup></code>
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.


**Follow up**: Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?


## Solution Explanation
To solve this problem in the most efficient way, I follow this step:

- Find `n`.
- Create a full list where all `n` distinct numbers are there.
- Convert this list to set.
- Convert the original `nums` list to set.
- Find the different between these two sets. This is also what we want to find.
