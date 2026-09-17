class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def solve():

            for r in range(9):
                for c in range(9):

                    if board[r][c] == '.':
                        box = (r // 3) * 3 + c // 3

                        for num in "123456789":

                            if (num not in rows[r] and
                                num not in cols[c] and
                                num not in boxes[box]):

                                # Place number
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box].add(num)

                                if solve():
                                    return True

                                # Backtrack
                                board[r][c] = '.'
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box].remove(num)

                        return False

            return True

        solve()