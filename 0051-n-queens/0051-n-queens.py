class Solution:
    def solveNQueens(self, n: int):
        ans = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):
            # All queens placed
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                # Check if queen can be placed
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return ans