class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        a1 = (ax2 - ax1) * (ay2 - ay1)
        a2 = (bx2 - bx1) * (by2 - by1)

        olw = max(0, min(ax2, bx2) - max(ax1, bx1))
        olh = max(0, min(ay2, by2) - max(ay1, by1))

        ola = olw* olh

        return a1 + a2 - ola