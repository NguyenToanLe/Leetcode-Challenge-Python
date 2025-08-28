# 2. Valid Parentheses
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`. determine if the input 
string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1**:
```
Input:      s = "( )"
Output:     true
```

**Example 2**:
```
Input:      s = "( ) [ ] { }"
Output:     true
```

**Example 3**:
```
Input:      s = "( ]"
Output:     false
```

**Example 4**:
```
Input:      s = "( [ ] )"
Output:     true
```

**Example 5**:
```
Input:      s = "( [ ) ]"
Output:     false
```

**Constraints:**
- <code>1 <= s.length <= 10<sup>4</sup></code>
- `s` consists of parentheses only `()[]{}`


## Solution Explanation
First, we need to overly estimate, whether the length of `s` is odd or even. In the case of odd length, return `False` 
immediately, because it will not enough character to construct pairs, which means at least an open or a close bracket 
will be missing.

Then we loop through every characters in `s`:

- If it is an open bracket, check if the next character its corresponding close bracket
  
    - If it is the case, remove both characters and loop through every characters in new, shorter `s`.
    - If the next character is not corresponding pair, continue to check next pair.

- If the current character is a close bracket, continue to the next character

If `s` is still a non-empty string and we reach the last character, this is the case where we can return `False`, because
we cannot find its corresponding pair anymore (if its pair stays before, this character should be already removed).

If `s` is an empty string at the end, that means we have enough bracket pairs and they are in correct position.
