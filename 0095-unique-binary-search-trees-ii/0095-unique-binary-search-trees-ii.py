class Solution:
    def generateTrees(self, n):

        def build(start, end):

            if start > end:
                return [None]

            result = []

            for root in range(start, end + 1):

                left_trees = build(start, root - 1)
                right_trees = build(root + 1, end)

                for left in left_trees:
                    for right in right_trees:

                        node = TreeNode(root)
                        node.left = left
                        node.right = right

                        result.append(node)

            return result

        return build(1, n)