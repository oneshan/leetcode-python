# 0146 - LRU Cache
# Date: 2022-10-19
# Runtime: 2212 ms, Memory: 76.7 MB
# Submission Id: 825898516


class LinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = LinkedNode(), LinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.table.get(key)
        if not node:
            return -1
        self._move_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.table.get(key)
        if node:
            node.val = value
            self._move_to_end(node)
            return
        
        node = LinkedNode(key, value)
        self.table[key] = node
        self._append_node(node)
        
        if self.size == self.capacity: # popleft
            head = self._pop_head()
            del self.table[head.key]
        else:
            self.size += 1
    
    def _delete_node(self, node):
        n_prev, n_next = node.prev, node.next
        n_prev.next = n_next
        n_next.prev = n_prev
        node.prev = node.next = None
    
    def _append_node(self, node):
        n_prev = self.tail.prev
        n_prev.next = node
        self.tail.prev = node
        node.prev = n_prev
        node.next = self.tail
    
    def _move_to_end(self, node):
        self._delete_node(node)
        self._append_node(node)
        
    def _pop_head(self):
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)