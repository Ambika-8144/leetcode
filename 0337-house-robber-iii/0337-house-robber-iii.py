# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root is None:
                return 0,0
            left=solve(root.left)
            right=solve(root.right)
            steal=root.val+left[1]+right[1] 
            skip=max(left[1],left[0])+max(right[1],right[0])
            return steal,skip
        steal,skip=solve(root)
        return max(steal,skip)
            
        