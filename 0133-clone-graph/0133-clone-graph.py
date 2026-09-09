class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        visited = {}

        def dfs(node):

            # Already cloned
            if node in visited:
                return visited[node]

            # Create clone
            clone = Node(node.val)

            # Store immediately
            visited[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)