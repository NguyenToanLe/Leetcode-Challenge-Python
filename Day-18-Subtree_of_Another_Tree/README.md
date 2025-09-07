# 18. Subtree of Another Tree
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same 
structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The 
tree `tree` could also be considered as a subtree of itself.

**Example 1**:

![Example 1](./ex1.jpg)
```
Input:        root = [3, 4, 5, 1, 1], subRoot = [4, 1, 2]
Output:       true
```

**Example 2**:

![Example 2](./ex2.jpg)
```
Input:        root = [3, 4, 5, 1, 2, null, null, null, null, 0], subRoot = [4, 1, 2]
Output:       false
```


**Constraints:**

- The number of the nodes in the `root` tree is in the range `[1, 2000]`.
- The number of the nodes in the `subRoot` tree is in the range `[1, 1000]`.
- <code>-10<sup>4</sup> <= root.val <= 10<sup>4</sup></code>
- <code>-10<sup>4</sup> <= subRoot.val <= 10<sup>4</sup></code>


## Solution Explanation
In this task, I reused the code in "Day 5: Same Tree".

I first checked if the `root` and `subRoot` is the same (with the reused function). If they are not the same, I 
recursively checked the left node or right node of `root` and `subRoot`.