class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:

            for t in range(1, k + 1):

                buy[t] = max(buy[t], sell[t - 1] - price)

                sell[t] = max(sell[t], buy[t] + price)

        return sell[k]