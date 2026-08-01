class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n, m = len(word1), len(word2)
        dp = [[-1] * m for _ in range(n)]

        def solve(i, j):

            if i == n:
                return m - j

            if j == m:
                return n - i

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = solve(i + 1, j + 1)
            else:
                insert = 1 + solve(i, j + 1)
                delete = 1 + solve(i + 1, j)
                replace = 1 + solve(i + 1, j + 1)

                dp[i][j] = min(insert, delete, replace)

            return dp[i][j]

        return solve(0, 0)