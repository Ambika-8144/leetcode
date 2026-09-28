class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        a= 0

        for ch in s:
            if ch == '(':
                d += 1
                a = max(a, d)

            elif ch == ')':
                d -= 1

        return a