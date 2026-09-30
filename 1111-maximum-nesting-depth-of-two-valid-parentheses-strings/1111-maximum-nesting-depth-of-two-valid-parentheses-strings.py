class Solution:
    def maxDepthAfterSplit(self, seq: str):
        ans = []
        depth = 0

        for ch in seq:

            if ch == '(':
                depth += 1
                ans.append(depth % 2)

            else:
                ans.append(depth % 2)
                depth -= 1

        return ans