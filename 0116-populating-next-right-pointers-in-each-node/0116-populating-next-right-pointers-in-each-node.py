class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        leftmost = root

        while leftmost.left:

            head = leftmost

            while head:

                # Connect left child → right child
                head.left.next = head.right

                # Connect right child → next node's left child
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root