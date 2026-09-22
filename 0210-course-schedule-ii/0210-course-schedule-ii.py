from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):

        # Build graph
        g = [[] for _ in range(numCourses)]

        # Calculate indegree
        id = [0] * numCourses

        for c, p in prerequisites:
            g[p].append(c)
            id[c] += 1

        # Courses with no prerequisites
        q= deque()

        for c in range(numCourses):
            if id[c] == 0:
                q.append(c)

        r = []

        # BFS
        while q:

            c = q.popleft()

            r.append(c)

            # Remove this course as a prerequisite
            for nc in g[c]:

                id[nc] -= 1

                # All prerequisites completed
                if id[nc] == 0:
                    q.append(nc)

        # If we couldn't process every course,
        # there is a cycle
        if len(r) != numCourses:
            return []

        return r