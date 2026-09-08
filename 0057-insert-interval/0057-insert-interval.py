class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        start, end = newInterval

        # 1. Intervals completely before newInterval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        # Add the merged/new interval
        result.append([start, end])

        # 3. Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result