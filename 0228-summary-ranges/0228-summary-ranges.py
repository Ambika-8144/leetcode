class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ans = []
        n = len(nums)
        i = 0

        while i < n:

            start = nums[i]

            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{end}")

            i += 1

        return ans