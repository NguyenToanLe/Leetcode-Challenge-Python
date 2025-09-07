

def countBits(n):
    # ans = []
    #
    # for num in range(n+1):
    #     bin_num = bin(num)[2:]
    #     bin_num_list = list(bin_num)
    #     bin_num_list = list(map(int, bin_num_list))
    #
    #     ans.append(sum(bin_num_list))
    #
    # return ans

    ans = [0] * (n + 1)

    for num in range(1, n+1):
        if num % 2 == 0:
            ans[num] = ans[num//2]
        else:
            ans[num] = ans[num - 1] + 1

    return ans


def main():
    n = 2
    print(f"n = {n}")
    print(f"expected output = [0, 1, 1]")
    print(f"output = {countBits(n)}")
    print("--" * 50)

    n = 5
    print(f"n = {n}")
    print(f"expected output = [0, 1, 1, 2, 1, 2]")
    print(f"output = {countBits(n)}")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
