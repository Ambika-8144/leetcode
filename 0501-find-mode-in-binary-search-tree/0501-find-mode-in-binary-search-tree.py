# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.count = 0
        self.maxCount = 0
        self.ans = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1

            if self.count > self.maxCount:
                self.maxCount = self.count
                self.ans = [node.val]
            elif self.count == self.maxCount:
                self.ans.append(node.val)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.ans