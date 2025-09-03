

def hammingWeight(n):
    bin_n = f"{n:032b}"
    bin_n_list = list(bin_n)
    bin_n_list = list(map(int, bin_n_list))

    return sum(bin_n_list)


def main():
    n = 11
    print(f"n = {n}")
    print(f"expected output = 3")
    count = hammingWeight(n)
    print(f"output = {count}")
    print(count == 3)
    print("--" * 50)

    n = 128
    print(f"n = {n}")
    print(f"expected output = 1")
    count = hammingWeight(n)
    print(f"output = {count}")
    print(count == 1)
    print("--" * 50)

    n = 2147483645
    print(f"n = {n}")
    print(f"expected output = 30")
    count = hammingWeight(n)
    print(f"output = {count}")
    print(count == 30)
    print("--" * 50)



if __name__ == '__main__':
    main()
    print("Finish")
