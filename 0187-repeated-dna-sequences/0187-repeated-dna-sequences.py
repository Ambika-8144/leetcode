class Solution:
    def findRepeatedDnaSequences(self, s: str):
        c= {}

        for i in range(len(s) - 9):
            sub = s[i:i+10]
            c[sub] = c.get(sub, 0) + 1

        r = []

        for sub in c:
            if c[sub] > 1:
                r.append(sub)

        return r