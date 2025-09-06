# 15. Valid Anagram
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given two strings `s` an `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original 
letters exactly once.

**Example 1**:

```
Input:          s = "anagram", t = "nagaram"
Output:         true
```

**Example 2**:

```
Input:          s = "rat", t = "car"
Output:         false
```


**Constraints:**

- <code>1 <= s.length, t.length <= 5 * 10<sup>5</sup></code>
- `s` and `t` consist of lowercase English letters.


## Solution Explanation
The idea to solve this problem is to count occurrence of each characters in both strings and compare their dictionaries
(or hash maps). 

We can reduce the running time by checking first the length of both strings, and then check differences during creating
hash maps of second string `t`.
