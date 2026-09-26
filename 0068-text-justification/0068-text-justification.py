class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        a = []
        i = 0

        while i < len(words):
            j = i
            ll = 0

            # Find how many words fit in this line
            while j < len(words):
                if ll + len(words[j]) + (j - i) <= maxWidth:
                    ll += len(words[j])
                    j += 1
                else:
                    break

            l = words[i:j]
            s = maxWidth - ll
            g = len(l) - 1

            # Last line OR only one word
            if j == len(words) or g == 0:
                r = " ".join(l)
                r += " " * (maxWidth - len(r))

            else:
                # Distribute spaces between words
                each = s // g
                extra = s % g

                r= ""

                for k in range(g):
                    r += l[k]
                    r += " " * (each + (1 if k < extra else 0))

                r += l[-1]

            a.append(r)
            i = j

        return a