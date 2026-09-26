class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        a = len(matrix)
        b = len(matrix[0])

        dp = [[0] * (b + 1) for _ in range(a + 1)]

        answer = 0

        for i in range(1, a+ 1):
            for j in range(1, b+ 1):

                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # top
                        dp[i][j - 1],      # left
                        dp[i - 1][j - 1]   # diagonal
                    )

                    answer = max(answer, dp[i][j])

        return answer * answer