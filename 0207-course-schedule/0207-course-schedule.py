class Solution:
    def canFinish(self, numCourses, prerequisites):

        g = [[] for _ in range(numCourses)]

        # Build graph
        for c, p in prerequisites:
            g[p].append(c)

        # 0 = not visited
        # 1 = currently visiting
        # 2 = completely processed
        s= [0] * numCourses

        def dfs(c):

            # Cycle found
            if s[c] == 1:
                return False

            # Already processed
            if s[c] == 2:
                return True

            # Mark as currently visiting
            s[c] = 1

            for nc in g[c]:

                if not dfs(nc):
                    return False

            # Completely processed
            s[c] = 2

            return True

        # Check every course
        for c in range(numCourses):

            if not dfs(c):
                return False

        return True