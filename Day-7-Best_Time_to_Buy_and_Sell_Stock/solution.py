

def maxProfit(prices):
    if len(prices) == 1:        # Buy and sell on the same day --> Zero profit
        return 0

    i = 0
    profit = 0
    buy = 0

    while i < len(prices) - 1:
        for i in range(buy, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                break
            if prices[i] - prices[buy] > profit:
                profit = prices[i] - prices[buy]

    return profit


def main():
    prices = [1, 7]
    print(f"prices = {prices}")
    print(f"expected output = 6")
    print(f"output = {maxProfit(prices)}")
    print("--" * 50)

    prices = [7,1,5,3,6,4]
    print(f"prices = {prices}")
    print(f"expected output = 5")
    print(f"output = {maxProfit(prices)}")
    print("--" * 50)

    prices = [7,6,4,3,1]
    print(f"prices = {prices}")
    print(f"expected output = 0")
    print(f"output = {maxProfit(prices)}")
    print("--" * 50)

    # prices = [7, 1, 5, 3, 6, 1]
    # remove_values(prices, 1)
    # print(prices)


if __name__ == '__main__':
    main()
    print("Finish")
