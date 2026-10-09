
class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        r = 0
        n = 0
        sn = 1

        for ch in s:
            if ch.isdigit():
                n = n * 10 + int(ch)

            elif ch == '+':
                r += sn * n
                n = 0
                sn = 1

            elif ch == '-':
                r += sn * n
                n = 0
                sn = -1

            elif ch == '(':
                stk.append(r)
                stk.append(sn)
                r = 0
                n = 0
                sn = 1

            elif ch == ')':
                r += sn * n
                n = 0
                r *= stk.pop()
                r += stk.pop()

        return r + sn * n
