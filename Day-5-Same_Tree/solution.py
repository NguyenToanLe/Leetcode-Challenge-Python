# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:      # If we reach here, one of two node is not None
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


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
