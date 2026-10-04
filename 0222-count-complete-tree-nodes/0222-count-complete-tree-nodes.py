'''class Solution:
    def countNodes(self, root):
        if root is None:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    '''
class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        l = root
        r = root

        lh = 0
        rh = 0

        while l:
            lh += 1
            l = l.left

        while r:
            rh += 1
            r = r.right

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
