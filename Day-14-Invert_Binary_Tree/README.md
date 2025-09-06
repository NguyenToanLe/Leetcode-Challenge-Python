# 14. Reverse Linked List
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given the `root` of a binary tree, invert the tree, and return *its root*.

**Example 1**:

![Example 1](./ex1.jpg)
```
Input:        root = [4, 2, 7, 1, 3, 6, 9]
Output:       [4, 7, 2, 9, 6, 3, 1]
```

**Example 2**:

![Example 2](./ex2.jpg)
```
Input:        root = [2, 1, 3]
Output:       [2, 3, 1]
```

**Example 3**:

```
Input:        root = []
Output:       []
```

**Constraints:**

- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`


## Solution Explanation
The idea of this task is to swap left child node and right child node at every node. But notice that we are not only 
swap left and child node, we also invert the left and right child nodes.
