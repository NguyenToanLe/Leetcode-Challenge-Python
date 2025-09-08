# 19. Longest Substring Without Repeating Characters
![Category](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Task

Given a string `s`, find the length of the **longest substring** without duplicate characters.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

**Example 1**:

```
Input:          s = "abcabcbb"
Output:         3
Explanation:    The answer is "abc", with the length of 3.
```

**Example 2**:

```
Input:          s = "bbbbb"
Output:         1
Explanation:    The answer is "b", with the length of 1.
```

**Example 3**:

```
Input:          s = "pwwkew"
Output:         3
Explanation:    The answer is "wke", with the length of 3.
                Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```


**Constraints:**

- <code>0 <= s.length <= 5 * 10<sup>4</sup></code>
- `s` consists of English letters, digits, symbols and spaces.



## Solution Explanation
For this task, I used 2 pointers `left_pt` and `right_pt`. A substring, hence, is built between these pointers (character
at `right_pt` is not inclusive).

I increase `right_pt` if the character at this position is not in the substring.

Otherwise, I increate `left_pt` by `1`, and hence, remove the first character in the substring.

If `right_pt` reach the last character in the original string, I stop the loop. Because the length will always reduce if
I continue. And this make no sense in find maximum length of substring.
