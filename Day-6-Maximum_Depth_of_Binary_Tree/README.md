# 6. Maximum Depth of Binary Tree
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest 
leaf node.

**Example 1**:

![Example 1](./ex1.jpg)
```
Input:        root = [3, 9, 20, null, null, 15, 7]
Output:       3
```

**Example 2**:

```
Input:        root = [1, null, 2]
Output:       2
```

**Constraints:**

- The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
- `-100 <= Node.val <= 100`


## Solution Explanation
I utilized recursion to solve this problem.

At every node, we just need to find the deeper depth of either left branch or right branch. The total depth of the whole 
tree will be this value extended by `1` (current plane).

If we reach the leaf, the depth will be `0`.
