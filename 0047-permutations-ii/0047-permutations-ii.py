class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        
        def backtrack(path, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack(path, used)
                
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return ans