# 11. Number of 1 Bits
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also 
known as the [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight)).

A set bit refers to a bit in the binary representation of a number that has a value of `1`.


**Example 1**:

```
Input:          n = 11
Output:         3
Explanation:    The input binary string 1011 has a total of three set bits.
```

**Example 2**:

```
Input:          n = 128
Output:         1
Explanation:    The input binary string 10000000 has a total of one set bit.
```

**Example 3**:

```
Input:          n = 2147483645
Output:         30
Explanation:    The input binary string 1111111111111111111111111111101  has a total of thirty set bits.
```

**Constraints:**

- <code>1 <= n <= 2<sup>31</sup> - 1</code>

**Follow up**: If this function is called many times, how would you optimize it?


## Solution Explanation
The steps are as following:

Convert to 32-bit string --> Convert this string to a list of character --> Convert list of strings to list of integers
--> Count total of `1` by sum up all integers in the list.
