class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):

                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(i + 1, current)

                current.pop()

        backtrack(0, [])

        return result
        