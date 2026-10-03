from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        words = set(wordList)

        q = deque()
        q.append((beginWord, 1))

        while q:

            w, c = q.popleft()

            for i in range(len(w)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    nw = w[:i] + ch + w[i+1:]

                    if nw == endWord:
                        return c + 1

                    if nw in words:
                        words.remove(nw)
                        q.append((nw, c + 1))

        return 0