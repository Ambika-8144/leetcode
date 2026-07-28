from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        length = 0
        odd = False

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd = True

        if odd:
            length += 1

        return length