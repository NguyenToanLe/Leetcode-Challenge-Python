# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.next = None

def hasCycle(head):
    current_node = head
    if current_node is None:        # Empty list
        return False
    if current_node.next is None:   # Reach the leaf
        return False

    traversed = []

    while True:
        if current_node in traversed:
            return True
        if current_node.next is None:       # Reach the leaf
            return False
        traversed.append(current_node)
        current_node = current_node.next


def main():
    pass
    # n = 2
    # print(f"n = {n}")
    # print(f"expected output = 2")
    # print(f"output = {climbStairs(n)}")
    # print("--" * 50)
    #
    # n = 3
    # print(f"n = {n}")
    # print(f"expected output = 3")
    # print(f"output = {climbStairs(n)}")
    # print("--" * 50)
    #
    # n = 4
    # print(f"n = {n}")
    # print(f"expected output = 5")
    # print(f"output = {climbStairs(n)}")
    # print("--" * 50)
    #
    # n = 5
    # print(f"n = {n}")
    # print(f"expected output = 8")
    # print(f"output = {climbStairs(n)}")
    # print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
