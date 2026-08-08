class Solution:
    def rob(self, nums: List[int]) -> int:
        '''def solve(i):
            if i>=len(nums):
                return 0 
            steal=nums[i]+solve(i+2)
            skip=solve(i+1)
            return max(steal,skip)
        return solve(0)'''
        dp=[-1]*len(nums)
        def solve(i):
            if i>=len(nums):
                return 0 
            if dp[i]!=-1:
                return dp[i]
            steal=nums[i]+solve(i+2)
            skip=solve(i+1)
            dp[i]=max(steal,skip)
            return dp[i]
        return solve(0)

        