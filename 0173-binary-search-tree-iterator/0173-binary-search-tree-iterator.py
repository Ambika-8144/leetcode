class BSTIterator:

    def __init__(self, root):
        self.arr = []
        self.inorder(root)
        self.i = 0

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)

    def next(self):
        val = self.arr[self.i]
        self.i += 1
        return val

    def hasNext(self):
        return self.i < len(self.arr)