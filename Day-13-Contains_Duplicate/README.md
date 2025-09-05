# 13. Contains Duplicate
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if
every element is distinct.

**Example 1**:

```
Input:          nums = [1, 2, 3, 1]
Output:         true
Explanation:    The element 1 occurs at the indices 0 and 3.
```

**Example 2**:

```
Input:          nums = [1, 2, 3, 4]
Output:         false
Explanation:    All elements are disctinct.
```

**Example 1**:

```
Input:          nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output:         true
```

**Constraints:**

- <code>1 <= nums.length <= 10<sup>5</sup></code>
- <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>


## Solution Explanation
I used `set` to remove all duplicates in the `list`. If there is at least a duplicate, the `len` of new `set` will **NOT**
be equal to the `len` of original `list`.
