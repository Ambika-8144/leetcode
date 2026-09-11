class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        mp = {}

        # Step 1: Create copy of every node
        curr = head

        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Connect next and random pointers
        curr = head

        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)

            curr = curr.next

        return mp[head]