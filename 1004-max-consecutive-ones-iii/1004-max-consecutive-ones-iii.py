class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #bruteforce 
        '''ans=0
        for i in range(len(nums)):
            zeros=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    zeros+=1
                if zeros>k:
                    break
                ans=max(ans,j-i+1)
        return ans '''
        #optimal
        l = zeros = ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans

        