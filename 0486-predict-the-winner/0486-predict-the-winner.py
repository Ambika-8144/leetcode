
from functools import lru_cache
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def solve(i, j):
            # Only one number left
            if i == j:
                return nums[i]

            # Pick left or right
            take_left = nums[i] - solve(i + 1, j)
            take_right = nums[j] - solve(i, j - 1)

            return max(take_left, take_right)

        return solve(0, len(nums) - 1) >= 0