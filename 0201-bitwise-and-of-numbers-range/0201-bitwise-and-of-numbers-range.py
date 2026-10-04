class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''a = left

        for i in range(left + 1, right + 1):
            a = a & i

        return a
        while right > left:
            right = right & (right - 1)

        return right'''
        s = 0

        while left != right:
            left >>= 1
            right >>= 1
            s += 1

        return left << s