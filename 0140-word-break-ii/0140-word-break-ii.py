class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        ws = set(wordDict)
        m = {}

        def dfs(i):

            if i == len(s):
                return [""]

            if i in m:
                return m[i]

            r= []

            for j in range(i + 1, len(s) + 1):

                word = s[i:j]

                if word in ws:

                    for sentence in dfs(j):

                        if sentence:
                            r.append(word + " " + sentence)
                        else:
                            r.append(word)

            m[i] = r
            return r

        return dfs(0)