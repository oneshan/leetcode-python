# 1903 - Design Most Recently Used Queue
# Date: 2024-05-27
# Runtime: 547 ms, Memory: 19.3 MB
# Submission Id: 1269416593


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class MRUQueue:

    def __init__(self, n: int):
        self.size = n
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        for i in range(1, n+1):
            node = ListNode(i)
            self._insert(node)
    
    def _insert(self, node):
        prev = self.tail.prev
        prev.next = self.tail.prev = node
        node.prev, node.next = prev, self.tail

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def fetch(self, k: int) -> int:
        curr = self.head
        for _ in range(k):
            curr = curr.next

        self._remove(curr)
        self._insert(curr)
        return curr.val

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)