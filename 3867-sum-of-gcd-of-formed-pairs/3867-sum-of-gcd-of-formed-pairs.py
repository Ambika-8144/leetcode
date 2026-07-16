class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxi, n = 0, len(nums)

        for i in range(n):

            maxi = max(maxi, nums[i])
            nums[i] = gcd(nums[i], maxi)

        nums.sort()

        return sum(gcd(nums[i], nums[~i]) for i in range(n // 2))

        