class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        # Valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # dp[i][j] = set of possible balances
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Starting cell
        if grid[0][0] == '(':
            dp[0][0].add(1)
        else:
            return False

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # Get balances from top and left
                possible = set()

                if i > 0:
                    possible |= dp[i - 1][j]

                if j > 0:
                    possible |= dp[i][j - 1]

                # Update balance based on current character
                for balance in possible:

                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Balance can never become negative
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        # At the end balance must be exactly 0
        return 0 in dp[m - 1][n - 1]