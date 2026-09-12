class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if board[r][c] != "O":
                return

            # Mark as safe
            board[r][c] = "E"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Check first and last rows
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)

            if board[m - 1][c] == "O":
                dfs(m - 1, c)

        # 2. Check first and last columns
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][n - 1] == "O":
                dfs(r, n - 1)

        # 3. Capture surrounded regions
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "E":
                    board[r][c] = "O"