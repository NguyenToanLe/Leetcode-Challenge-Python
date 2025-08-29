

def climbStairs(n):
    import math
    def arrangement(n, k):
        per = math.perm(n, k)
        return int(per / math.factorial(k))

    number_of_2 = 0
    total_ways = 0
    while 2*number_of_2 <= n:
        number_of_1 = n - 2*number_of_2
        total_ways += arrangement(number_of_1 + number_of_2, number_of_2)
        number_of_2 += 1

    return total_ways


def main():
    n = 2
    print(f"n = {n}")
    print(f"expected output = 2")
    print(f"output = {climbStairs(n)}")
    print("--" * 50)

    n = 3
    print(f"n = {n}")
    print(f"expected output = 3")
    print(f"output = {climbStairs(n)}")
    print("--" * 50)

    n = 4
    print(f"n = {n}")
    print(f"expected output = 5")
    print(f"output = {climbStairs(n)}")
    print("--" * 50)

    n = 5
    print(f"n = {n}")
    print(f"expected output = 8")
    print(f"output = {climbStairs(n)}")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
