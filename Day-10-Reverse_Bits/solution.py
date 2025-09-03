

def reverseBits(n):
    bin_n = f"{n:032b}"
    reverse_bin_n = bin_n[::-1]
    reverse_n = int(reverse_bin_n, 2)

    return reverse_n


def main():
    n = 43261596
    print(f"n = {n}")
    print(f"expected output = 964176192")
    reverse = reverseBits(n)
    print(f"output = {reverse}")
    print(reverse == 964176192)
    print("--" * 50)

    n = 2147483644
    print(f"n = {n}")
    print(f"expected output = 1073741822")
    reverse = reverseBits(n)
    print(f"output = {reverse}")
    print(reverse == 1073741822)
    print("--" * 50)



if __name__ == '__main__':
    main()
    print("Finish")
