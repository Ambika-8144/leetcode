class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #bruteforce/better
        '''a=nums[0]
        for i in range(len(nums)):
            p=1
            for j in range(i,len(nums)):
                p*=nums[j]
                a=max(a,p)
        return a'''
        #optimal solution
        n = len(nums)
        prefix = 1
        suffix = 1
        ans = nums[0]

        for i in range(n):

                # Prefix
            if prefix == 0:
                prefix = 1

            prefix *= nums[i]

                # Suffix
            if suffix == 0:
                suffix = 1

            suffix *= nums[n - 1 - i]

            ans = max(ans, prefix, suffix)

        return ans

            