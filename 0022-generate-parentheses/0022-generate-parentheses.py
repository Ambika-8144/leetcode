class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def backtrack(curr, open, close):

            if len(curr) == 2 * n:
                ans.append(curr)
                return

            # Add '('
            if open < n:
                backtrack(curr + "(", open + 1, close)

            # Add ')'
            if close < open:
                backtrack(curr + ")", open, close + 1)

        backtrack("", 0, 0)
        return ans