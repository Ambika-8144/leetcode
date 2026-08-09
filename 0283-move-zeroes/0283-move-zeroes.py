class Solution:
    def moveZeroes(self, nums):
        '''j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1'''
        #bruteforce tc:O(n) and sc:O(n)
        '''non_zero=[]
        for num in nums:
            if num!=0:
                non_zero.append(num)
        for i in range(len(non_zero)):
            nums[i]=non_zero[i]
        for i in range(len(non_zero),len(nums)):
            nums[i]=0
        return nums'''
        # optimal 2 pointer 
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
        
        