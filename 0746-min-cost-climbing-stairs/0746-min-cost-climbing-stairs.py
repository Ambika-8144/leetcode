class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [-1] * len(cost)

        def solve(i):

            if i >= len(cost):
                return 0

            if dp[i] != -1:
                return dp[i]

            one_step = cost[i] + solve(i + 1)
            two_step = cost[i] + solve(i + 2)

            dp[i] = min(one_step, two_step)

            return dp[i]

        return min(solve(0), solve(1))