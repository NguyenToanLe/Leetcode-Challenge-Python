# 10. Reverse Bits
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Reverse bits of a given 32 bits signed integer.

**Example 1**:

> **Input**     n = 43261596
> 
> **Output**    964176192
> 
> | Integer   | Binary                           |
> |-----------|----------------------------------|
> | 43261596  | 00000010100101000001111010011100 |
> | 964176192 | 00111001011110000010100101000000 |

**Example 1**:

> **Input**     n = 2147483644
> 
> **Output**    1073741822
> 
> | Integer    | Binary                           |
> |------------|----------------------------------|
> | 2147483644 | 01111111111111111111111111111100 |
> | 1073741822 | 00111111111111111111111111111110 |

**Constraints:**

- <code>0 <= n <= 2<sup>31</sup> - 2</code>
- `n` is even.

**Follow up**: If this function is called many times, how would you optimize it?


## Solution Explanation
The steps are as following:

Convert to 32-bit --> Reverse this string --> Convert back to integer.
