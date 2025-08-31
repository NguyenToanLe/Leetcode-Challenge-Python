# 5. Same Tree
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1**:

![Example 1](./ex1.jpg)
```
Input:        p = [1, 2, 3], q = [1, 2, 3]
Output:       true
```

**Example 2**:

![Example 2](./ex2.jpg)
```
Input:        p = [1, 2], q = [1, null, 2]
Output:       false
```

**Example 3**:

![Example 3](./ex3.jpg)
```
Input:        p = [1, 2, 1], q = [1, 1, 3]
Output:       false
```

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`
- <code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code>


## Solution Explanation
I utilized recursion to solve this problem.

Two Tree is the same iff:

- Current node of First tree is the same as Current node of Second tree in their Value
- Left node of First tree is the same as Left node of Second tree
- Right node of First tree is the same as Right node of Second tree
- If one of two tree reaches its leaf, the other tree MUST also reaches its leaf. 
