
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True)
        k = k1 + k2
        n = len(d)

        if sum(d) <= k:
            return 0

        d.append(0)

        for i in range(n):
            cost = (d[i] - d[i + 1]) * (i + 1)

            if cost <= k:
                k -= cost
            else:
                q, r = divmod(k, i + 1)
                level = d[i] - q
                return sum(x * x for x in d[i + 1:]) + (i + 1 - r) * level**2 + r * (level - 1)**2

        return 0
