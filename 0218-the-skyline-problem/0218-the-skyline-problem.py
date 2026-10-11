import heapq
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        '''res = []
        ph = 0

        s = buildings[0][0]
        e = max(b[1] for b in buildings)

        for x in range(s, e + 1):
            mh = 0

            for l, r, h in buildings:
                if l <= x < r:
                    mh = max(mh, h)

            if mh != ph:
                res.append([x, mh])
                ph = mh

        return res'''
        res = []
        ph = 0
        e = []

        for l, r, h in buildings:
            e.append((l, -h, r))
            e.append((r, 0, 0))

        e.sort()
        h = [(0, float('inf'))]

        for x, nh, r in e:
            while h[0][1] <= x:
                heapq.heappop(h)

            if nh:
                heapq.heappush(h, (nh, r))

            mh = -h[0][0]

            if mh != ph:
                res.append([x, mh])
                ph = mh
        return res