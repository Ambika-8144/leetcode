# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # Last node of each level
            ans.append(node.val)

        return ans

