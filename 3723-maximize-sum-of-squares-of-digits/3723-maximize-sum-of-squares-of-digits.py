
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        res = []

        while sum >= 9:
            res.append('9')
            sum -= 9

        if sum > 0:
            res.append(str(sum))

        while len(res) < num:
            res.append('0')

        return ''.join(res)
