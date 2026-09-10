class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None

        # Find middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node

        # Disconnect left half from middle
        if prev:
            prev.next = None
        else:
            # Only one node
            head = None

        # Middle becomes root
        root = TreeNode(slow.val)

        # Recursively build left and right
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root