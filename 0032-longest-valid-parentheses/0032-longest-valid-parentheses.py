class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stk = [-1]
        maxi = 0

        for i in range(len(s)):

            if s[i] == '(':
                stk.append(i)

            else:
                stk.pop()

                if not stk:
                    stk.append(i)
                else:
                    maxi = max(maxi, i - stk[-1])

        return maxi