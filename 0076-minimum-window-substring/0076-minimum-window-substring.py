class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        n = {}

        for ch in t:
            n[ch] = n.get(ch, 0) + 1

        w = {}

        l = 0
        h = 0
        nc = len(n)

        ml= float('inf')
        r = ""

        for rt in range(len(s)):

            ch = s[rt]

            w[ch] = w.get(ch, 0) + 1

            # Character satisfied its required frequency
            if ch in n and w[ch] == n[ch]:
                h += 1

            # Window is valid
            while h == nc:

                # Update minimum window
                if rt - l + 1 < ml:
                    ml = rt - l + 1
                    r = s[l:rt + 1]

                # Remove left character
                lch = s[l]
                w[lch] -= 1

                # Window became invalid
                if lch in n and w[lch] < n[lch]:
                    h -= 1

                l += 1

        return r