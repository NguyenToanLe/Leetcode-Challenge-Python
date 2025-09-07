

def missingNumber(nums):
    n = len(nums)

    full_set = set(range(n+1))
    nums_set = set(nums)

    diff = full_set - nums_set

    return diff.pop()


def main():
    nums = [3,0,1]
    print(f"nums = {nums}")
    print(f"expected output = 2")
    print(f"output = {missingNumber(nums)}")
    print("--" * 50)

    nums = [0, 1]
    print(f"nums = {nums}")
    print(f"expected output = 2")
    print(f"output = {missingNumber(nums)}")
    print("--" * 50)

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"nums = {nums}")
    print(f"expected output = 8")
    print(f"output = {missingNumber(nums)}")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
