class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Try each character as the starting character
        for c in range(26):

            if first[c] == n:
                continue

            l = first[c]
            r = last[c]

            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character started before l,
                # so substring cannot be valid
                if first[x] < l:
                    valid = False
                    break

                # Need to include all occurrences
                r = max(r, last[x])

                i += 1

            if valid:
                intervals.append((l, r))

        # Greedy: choose intervals with smallest ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans