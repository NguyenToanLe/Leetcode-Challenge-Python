# 12. Reverse Linked List
![Category](https://img.shields.io/badge/Difficulty-Easy-green)

## Task

Given the `head` of a singly linked list, reverse the list, and return the *reversed list*.

**Example 1**:

![Example 1](./ex1.jpg)
```
Input:        head = [1, 2, 3, 4, 5]
Output:       [5, 4, 3, 2, 1]
```

**Example 2**:

![Example 2](./ex2.jpg)
```
Input:        head = [1, 2]
Output:       [2, 1]
```

**Example 2**:

```
Input:        head = []
Output:       []
```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up**: A linked list can be reversed either iteratively or recursively. Could you implement both?


## Solution Explanation
I just can solve this Leetcode by using iterative approach.

First I save all nodes into a normal list. Then I reverse the list. From this points, I already have the "reversed 
linked list". All I have to do now is to adjust the connected node.

Currently, the node `i` is connecting to node `i-1`, I just have to connect the node `i` to node `i+1`. 

Finally, I connect the last node to an empty node `None`, and return the first node as new `head`.
