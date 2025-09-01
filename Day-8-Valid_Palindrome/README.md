# 8. Valid Palindrome
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a* ***palindrome*** *, or* `false` *otherwise*.

**Example 1**:

```
Input:        s = "A man, a plan, a canal: Panama"
Output:       true
Explanations: "amanaplanacanalpanama" is a palindrome.
```

**Example 2**:

```
Input:        s = "race a car"
Output:       false
Explanations: "raceacar" is not a palindrome.
```

**Example 3**:

```
Input:        s = " "
Output:       true
Explanations: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints:**

- <code>1 <= s.length <= 2 * 10<sup>5</sup></code>
- `s` consists only of printable ASCII characters.


## Solution Explanation

If the string just has one character, return `True`

Then, I use `re` library to find all non-alphanumeric characters and replace them by `''` empty string.

Finally, I just compare the first and last characters pairwise. If we meet a unequal pair, return `False`.
