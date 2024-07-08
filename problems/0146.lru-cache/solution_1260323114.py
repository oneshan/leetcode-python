# 0146 - LRU Cache
# Date: 2024-05-17
# Runtime: 566 ms, Memory: 77.7 MB
# Submission Id: 1260323114


class ListNode:
    def __init__(self, key, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.remains = capacity
        self.table = {}  # key: node
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self._remove(node) 
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.val = value
            self._remove(node) 
            self._append(node)
            self.table[key] = node
            return

        if self.remains == 0:
            node = self.head.next
            self._remove(node)
            self.table.pop(node.key)
        else:
            self.remains -= 1

        node = ListNode(key, value)
        self.table[key] = node
        self._append(node)

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _append(self, node):
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)