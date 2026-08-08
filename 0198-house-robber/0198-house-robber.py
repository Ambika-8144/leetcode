class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursion approach
        '''def solve(i):
            if i>=len(nums):
                return 0 
            steal=nums[i]+solve(i+2)
            skip=solve(i+1)
            return max(steal,skip)
        return solve(0)'''
        #recursion + memoization approach
        '''dp=[-1]*len(nums)
        def solve(i):
            if i>=len(nums):
                return 0 
            if dp[i]!=-1:
                return dp[i]
            steal=nums[i]+solve(i+2)
            skip=solve(i+1)
            dp[i]=max(steal,skip)
            return dp[i]
        return solve(0)'''
        #bottom-up approach 
        dp=[-1]*(len(nums)+1)
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,len(nums)+1):
            dp[i]=max((nums[i-1]+dp[i-2]),dp[i-1])
        return dp[len(nums)]
        