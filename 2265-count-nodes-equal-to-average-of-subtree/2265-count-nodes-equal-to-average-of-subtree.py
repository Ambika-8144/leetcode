class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans = 0

        def dfs(node):
            nonlocal ans

            if node is None:
                return 0, 0

            # Get sum and count from left subtree
            left_sum, left_count = dfs(node.left)

            # Get sum and count from right subtree
            right_sum, right_count = dfs(node.right)

            # Include current node
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # Calculate average
            average = total_sum // total_count

            if node.val == average:
                ans += 1

            return total_sum, total_count

        dfs(root)

        return ans