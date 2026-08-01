from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []

        def backtrack(start, path, total):

            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return

            if total > n:
                return

            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()

        backtrack(1, [], 0)

        return ans