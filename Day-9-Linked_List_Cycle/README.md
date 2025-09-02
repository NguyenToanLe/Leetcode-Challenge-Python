# 9. Linked List Cycle
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following 
the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to.
**Note that** `pos` **is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1**:

![Example 1](./ex1.png)
```
Input:        head = [3, 2, 0, -4], pos = 1
Output:       true
Explanation:  There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2**:

![Example 2](./ex2.png)
```
Input:        head = [1, 2], pos = 0
Output:       true
Explanation:  There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3**:

![Example 3](./ex3.png)
```
Input:        head = [1], pos = -1
Output:       false
Explanation:  There is no cycle in the linked list.
```

**Constraints:**

- The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
- <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up**: Can you solve it using `O(1)` (i.e.e constant) memory?


## Solution Explanation
I utilized recursion to solve this problem.

At every node, we just need to find the deeper depth of either left branch or right branch. The total depth of the whole 
tree will be this value extended by `1` (current plane).

If we reach the leaf, the depth will be `0`.
