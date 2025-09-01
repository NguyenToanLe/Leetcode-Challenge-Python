# 7. Best Time to Buy and Sell Stock
![Category](https://img.shields.io/badge/Difficulty-Easy-green)
![Category](https://img.shields.io/badge/Personal-Medium-yellow)

## Task

You are given an array `prices` where `prices[i]` is the price of a given stock on the <code>i<sup>th</sup></code> day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the 
future** to sell that stock.

Return that *maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Example 1**:

```
Input:        prices = [7, 1, 5, 3, 6, 4]
Output:       5
Explanation:  Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2**:

```
Input:        prices = [7, 6, 4, 3, 1]
Output:       0
Explanation:  In this case, no transactions are done and the max profit = 0.
```

**Constraints:**

- <code>1 <= prices.length <= 10<sup>5</sup></code>
- <code>0 <= prices[i] <= 10<sup>4</sup></code>


## Solution Explanation

1. Initialize a `buy=0` variable. This is the index of the buying price.
2. Then iterate from the next index to the end of the list.
3. If we meet a price that lower than `prices[buy]`, which means this should be the buying price now, we update the `buy`
variable with this new index and rerun the loop from step 2.

During looping, when the difference between current price and buying price (profit) is greater the maximum profit, update 
the maximum profit. This is also the return value.
