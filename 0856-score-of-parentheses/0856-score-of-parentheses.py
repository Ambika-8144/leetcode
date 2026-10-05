class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]

        for ch in s:
            if ch == '(':
                stk.append(0)
            else:
                v = stk.pop()

                if v == 0:
                    v = 1
                else:
                    v = 2 * v

                stk[-1] += v

        return stk[0]