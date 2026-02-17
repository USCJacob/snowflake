class MinStack:

    class Node:
        def __init__(self, val, cur_min, nxt):
            self.val = val
            self.min = cur_min
            self.next = nxt

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = self.Node(val, val, None)
        else:
            self.head = self.Node(val, min(val, self.head.min), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min