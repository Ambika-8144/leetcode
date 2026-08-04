class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        f=min(nums)
        l=max(nums)
        a=[]
        for i in range(f,l+1):
            if i not in nums:
                a.append(i)
        return a

        