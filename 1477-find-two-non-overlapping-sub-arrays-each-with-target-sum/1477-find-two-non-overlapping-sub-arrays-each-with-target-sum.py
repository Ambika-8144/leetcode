class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        best = [INF] * n
        left = 0
        total = 0
        min_len = INF
        ans = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                # Previous non-overlapping subarray
                if left > 0:
                    ans = min(ans, length + best[left - 1])

                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if ans == INF else ans