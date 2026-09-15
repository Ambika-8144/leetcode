class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)

        curr = head

        while curr:
            next_node = curr.next

            prev = dummy

            # Find the correct position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            curr = next_node

        return dummy.next