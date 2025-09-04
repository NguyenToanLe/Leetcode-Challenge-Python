# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.next = None

def reverseList_iterative(head):
    if head is None:
        return head

    reversed_list = []
    current_node = head

    while current_node is not None:
        reversed_list.append(current_node)
        current_node = current_node.next

    reversed_list.reverse()

    for i in range(len(reversed_list) - 1):
        reversed_list[i].next = reversed_list[i+1]

    reversed_list[-1].next = None

    return reversed_list[0]


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
