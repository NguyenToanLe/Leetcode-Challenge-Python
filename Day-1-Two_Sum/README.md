# 1. Two Sum
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to 
`target`*. 

You may assume that each input would have ***exactly one solution***, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1**:
```
Input:          nums = [2, 7, 11, 15], target = 9
Output:         [0, 1]
Explanation:    Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2**:
```
Input:          nums = [3, 2, 4], target = 6
Output:         [1, 2]
```

**Example 3**:
```
Input:          nums = [3, 3], target = 6
Output:         [0, 1]
```

**Constraints:**
- <code>2 <= nums.length <= 10<sup>4</sup></code>
- <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>
- <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code>
- **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorith that is less than <code>O(n<sup>2</sup>)</code> time complexity?

## Solution Explanation
Assume that the `target` is summed up from two numbers `a` and `b`. I first iterate `a` over the `nums` list and 
determine, whether `b=target-a` is in the rest of the list (`nums` with `a` removed). If the answer is yes, return the 
index of `a` and `b`. If the answer is no, return `[None, None]`

Some points to notice:

- Because there exists ***exactly*** one solution, `a` and `b` will always be found. Hence, the last line in the function
is redundant.
- Notice that the index of `b` is referenced in `nums` list, not in the truncated one. But this can be found via the
truncated one. If the found index is bigger or equal to the `a`'s index, `b` needs to be to the right of `a` in `nums` 
list. 
