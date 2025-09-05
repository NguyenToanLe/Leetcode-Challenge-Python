

def containsDuplicate(nums):
    set_nums = set(nums)

    if len(set_nums) != len(nums):      # There is duplicate
        return True
    else:
        return False



def main():
    nums = [1, 2, 3, 1]
    print(f"nums = {nums}")
    print(f"expected output = true")
    print(f"output = {containsDuplicate(nums)}")
    print("--" * 50)

    nums = [1, 2, 3, 4]
    print(f"nums = {nums}")
    print(f"expected output = false")
    print(f"output = {containsDuplicate(nums)}")
    print("--" * 50)

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"nums = {nums}")
    print(f"expected output = true")
    print(f"output = {containsDuplicate(nums)}")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
