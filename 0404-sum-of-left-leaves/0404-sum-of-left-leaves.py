class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, isLeft):
            if not node:
                return 0

            if not node.left and not node.right:
                return node.val if isLeft else 0

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)