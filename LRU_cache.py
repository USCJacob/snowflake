class Node:
    def __init__(self, key = -1, value = -1):
        self.key, self.value = key, value
        self.prev, self.next = None, None
class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.d = {}

    def _delete(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _append(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self._delete(n)
            self._append(n)
            return n.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._delete(self.d[key])
        n = Node(key, value)
        self._append(n)
        self.d[key] = n
        if len(self.d) > self.capacity:
            n = self.head.next
            self._delete(n)
            del self.d[n.key]