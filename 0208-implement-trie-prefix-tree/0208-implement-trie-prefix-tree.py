class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        current = self

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Trie()

            current = current.children[ch]

        current.end = True

    def search(self, word: str) -> bool:
        current = self

        for ch in word:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self

        for ch in prefix:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return True