class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        ans = []

        while num:
            ans.append(str(num % 7))
            num //= 7

        ans = "".join(ans[::-1])

        return "-" + ans if negative else ans