class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            ds= 0

            while n > 0:
                ds+= n % 10
                n //= 10

            if ds== i:
                return i

        return -1