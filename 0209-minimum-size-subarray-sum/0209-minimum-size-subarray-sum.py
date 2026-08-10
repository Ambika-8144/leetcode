class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''n=len(nums)
        ans=float('inf')
        for i in range(n):
            total = 0
            for j in range(i,n):
                total += nums[j]

                if total >= target:
                    ans = min(ans,j-i+1)
                    break 
        return 0 if ans==float('inf') else ans'''
        #better solution 
        from bisect import bisect_left
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        ans=float('inf')
        for i in range(n):
            diff=target+prefix[i]
            j=bisect_left(prefix,diff)
            if j<len(prefix):
                ans=min(ans,j-i)
        return 0 if ans==float('inf') else ans
        