class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        result = []
        path = []

        def dfs(node, remaining):

            if not node:
                return

            # Add current node
            path.append(node.val)

            # Check if current node is a leaf
            if node.left is None and node.right is None:
                if remaining == node.val:
                    result.append(path.copy())

            else:
                # Explore left and right
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)

            # Backtrack
            path.pop()

        dfs(root, targetSum)

        return result