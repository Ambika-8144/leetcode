class Solution:
    def moveZeroes(self, nums):
        '''j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1'''
        #bruteforce 
        non_zero=[]
        for num in nums:
            if num!=0:
                non_zero.append(num)
        for i in range(len(non_zero)):
            nums[i]=non_zero[i]
        for i in range(len(non_zero),len(nums)):
            nums[i]=0
        return nums
        