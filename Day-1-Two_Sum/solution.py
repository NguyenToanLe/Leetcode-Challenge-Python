

def twoSum(nums, target):
    for i in range(len(nums)):
        nums_truncated = nums.copy()
        del nums_truncated[i]
        rest = target - nums[i]
        if rest in nums_truncated:
            ind = nums_truncated.index(rest)          # [1, 2, 3, <4>, <5>, 6, 7] and 9
            if ind >= i:
                ind += 1
            if i < ind:
                return [i, ind]
            else:
                return [ind, i]

    return [None, None]         # This line is redundant


def main():
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))
    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))
    nums3 = [3, 3]
    target3 = 6
    print(twoSum(nums3, target3))


if __name__ == '__main__':
    main()
    print("Finish")
