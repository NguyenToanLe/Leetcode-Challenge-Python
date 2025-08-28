# 3. Merge Two Sorted Lists
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two 
lists.

Return *the head of the merged linked list*.

**Example 1**:

![Example 1](example.jpg)

```
Input:      list1 = [1,2,4], list2 = [1,3,4]
Output:     [1,1,2,3,4,4]
```

**Example 2**:
```
Input:      list1 = [], list2 = []
Output:     []
```

**Example 3**:
```
Input:      list1 = [], list2 = [0]
Output:     [0]
 
```

**Constraints:**
- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.


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
