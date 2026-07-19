class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}

        # Store last occurrence of each character
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):

            if ch in visited:
                continue

            while (stack and
                   ch < stack[-1] and
                   last[stack[-1]] > i):

                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)