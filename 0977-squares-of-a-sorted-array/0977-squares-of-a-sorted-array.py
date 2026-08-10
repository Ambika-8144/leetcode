class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #bruteforce 
        '''for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        return sorted(nums)'''
        #better 
        n=len(nums)
        result=[0]*n
        left=0 
        right=n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left])>abs(nums[right]):
                result[i]=abs(nums[left])**2
                left+=1
            else:
                result[i]=abs(nums[right])**2
                right-=1
        return result         