class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = [""]

        for ch in s:
            if ch == '(':
                st.append("")
            elif ch == ')':
                t = st.pop()
                t= t[::-1]
                st[-1] += t
            else:
                st[-1] += ch

        return st[0]