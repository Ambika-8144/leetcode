class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        ans = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                j = i + 1

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                if key in mp:
                    ans.append(mp[key])
                else:
                    ans.append('?')

                i = j + 1

            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)