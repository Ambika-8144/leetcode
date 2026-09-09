class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # 1. Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        # 3. Merge two halves
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next