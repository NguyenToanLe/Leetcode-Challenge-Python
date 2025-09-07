# 17. Counting Bits
![Category](https://img.shields.io/badge/Difficulty-Easy-green)
![Category](https://img.shields.io/badge/Optimization-Medium-yellow)

## Task

Given an integer `n`, return *an array* `ans` *of length* `n + 1` *such that for each* `i` (`0 <= i <= n`), `ans[i]` *is
the* ***number of*** `1`***'s*** *in the binary*.

**Example 1**:

```
Input:          n = 2
Output:         [0, 1, 1]
Explanation:    0 --> 0
                1 --> 1
                2 --> 10
```

**Example 2**:

```
Input:          n = 5
Output:         [0, 1, 1, 2, 1, 5]
Explanation:    0 --> 0
                1 --> 1
                2 --> 10
                3 --> 11
                4 --> 100
                5 --> 101
```


**Constraints:**

- <code>0 <= n <= 10<sup>5</sup></code>


**Follow up**: 
- It is very easy to come up with a solution with a runtime of `O(n logn)`. Can you do it in linear time `O(n)` and 
possibly in a single pass?
- Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?


## Solution Explanation
### Weak solution

I iterated from `0` to `n`. At each step, I do following things:

- Convert this number to binary string.
- Convert this string to a list.
- Convert each string element in list to integer.
- Sum all element in the list to count set bits in this current number.

### Optimized solution
There are two observations:

1. If the current number `n` is even, in the binary form, it is the number `n/2` with all binary bits shifted to the left
2. If the current number `n` is odd, the number of set bits is equal the number of set bits of `n-1` increased by `1`.

To explain the first observation, I take an example:

`n = 12 = 2^3 + 2^2 --> 01100`

`n = 6 = 12 / 2 = (2^3 + 2^2) / 2 = 2^2 + 2^1 --> 00110`

For the first observation, to increase a number by one, we add `1` to this number. This means we turn the last bit to `1`. 
This also means we increase the number of set bits by `1`.
