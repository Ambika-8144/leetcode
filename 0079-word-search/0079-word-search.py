class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):
            # All characters matched
            if k == len(word):
                return True

            # Out of bounds or wrong character
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[k]:
                return False

            # Mark as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore 4 directions
            found = (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            # Backtrack
            board[i][j] = temp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False