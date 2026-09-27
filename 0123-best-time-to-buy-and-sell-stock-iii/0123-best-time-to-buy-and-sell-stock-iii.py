class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        b1= float('-inf')
        s1= 0
        b2 = float('-inf')
        s2 = 0

        for p in prices:
            b1 = max(b1, -p)
            s1 = max(s1, b1 + p)

            b2 = max(b2, s1 - p)
            s2 = max(s2, b2 + p)

        return s2