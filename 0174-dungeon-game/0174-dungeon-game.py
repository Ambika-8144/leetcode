class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])

                elif i == m - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])

                elif j == n - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])

                else:
                    next_hp = min(dp[i + 1][j], dp[i][j + 1])
                    dp[i][j] = max(1, next_hp - dungeon[i][j])

        return dp[0][0]