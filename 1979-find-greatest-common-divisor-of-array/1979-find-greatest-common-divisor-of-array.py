class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s=min(nums)
        l=max(nums)
        if s==0:
            return l 
        while s!=0:
            l,s=s,l%s
        return l
        