class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursion approach
        '''def solve(i,end):
            if i>=end:
                return 0 
            steal=nums[i]+solve(i+2,end)
            skip=solve(i+1,end)
            return max(steal,skip)
        n=len(nums)
        if n==1:
            return nums[0]
        dp1=solve(0,n-1)
        dp2=solve(1,n)
        return max(dp1,dp2)'''
        #recursion +memoization 

        '''def solve(i,end,dp):
            if i>=end:
                return 0 
            if dp[i]!=-1:
                return dp[i]
            steal=nums[i]+solve(i+2,end,dp)
            skip=solve(i+1,end,dp)
            dp[i]=max(steal,skip)
            return dp[i]
        n=len(nums)
        if n==1:
            return nums[0]
        d1=[-1]*n
        d2=[-1]*n
        dp1=solve(0,n-1,d1)
        dp2=solve(1,n,d2)
        return max(dp1,dp2)'''
        #bottom-up approach 
        def solve(start, end):
            dp = [0] * (end - start + 1)
            dp[0] = 0
            dp[1] = nums[start]
            for i in range(2, end - start + 1):
                dp[i] = max(nums[start + i - 1] + dp[i-2],dp[i-1])
            return dp[-1]
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = solve(0, n - 1)
        dp2 = solve(1, n)
        return max(dp1, dp2)