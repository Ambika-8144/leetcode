class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        digits = "0123456789abcdef"

        num &= 0xffffffff

        ans = []

        while num:
            ans.append(digits[num & 15])
            num >>= 4

        return "".join(reversed(ans))