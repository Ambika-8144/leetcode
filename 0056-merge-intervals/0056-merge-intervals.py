class Solution:
    def merge(self, intervals):
        intervals.sort()
        ans = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans