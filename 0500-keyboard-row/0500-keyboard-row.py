class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        ans = []

        for word in words:
            w = word.lower()

            if all(ch in row1 for ch in w) or \
               all(ch in row2 for ch in w) or \
               all(ch in row3 for ch in w):
                ans.append(word)

        return ans