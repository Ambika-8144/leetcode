class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #bruteforce solution 
        count0=0
        count1=0
        count2=0
        for num in nums :
            if num==0:
                count0+=1
            elif num==1:
                count1+=1
            else :
                count2+=1
        i=0
        while count0>0:
            nums[i]=0
            count0-=1
            i+=1
        while count1>0:
            nums[i]=1
            count1-=1
            i+=1
        while count2>0:
            nums[i]=2
            count2-=1
            i+=1
        

        