class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)

        small_curr = small
        large_curr = large

        curr = head

        while curr:
            if curr.val < x:
                small_curr.next = curr
                small_curr = small_curr.next
            else:
                large_curr.next = curr
                large_curr = large_curr.next

            curr = curr.next

        # Connect small list to large list
        small_curr.next = large.next

        # Important: terminate the large list
        large_curr.next = None

        return small.next