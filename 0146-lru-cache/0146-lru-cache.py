class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)    # LRU side
        self.right = Node(0, 0)   # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert node at MRU position
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)
        self.cache[key] = node

        # Add to MRU
        self.insert(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            # First node after left = LRU
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]