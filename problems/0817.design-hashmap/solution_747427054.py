# 0817 - Design HashMap
# Date: 2022-07-15
# Runtime: 533 ms, Memory: 18.4 MB
# Submission Id: 747427054


class MyHashMap:

    def __init__(self):
        self.key_range = 769
        self.bucket = [Bucket() for _ in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range
    
    def put(self, key: int, value: int) -> None:
        bucket = self.bucket[self._hash(key)]
        bucket.put(key, value)

    def get(self, key: int) -> int:
        bucket = self.bucket[self._hash(key)]
        return bucket.get(key)

    def remove(self, key: int) -> None:
        bucket = self.bucket[self._hash(key)]
        bucket.remove(key)

        
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class Bucket:
    def __init__(self):
        self.head = Node(0, 0)
    
    def put(self, key, val):
        node = self.head
        while node.next:
            if node.next.key == key:
                node.next.val = val
                return
            node = node.next
        node.next = Node(key, val)
        
    def get(self, key):
        node = self.head
        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next
        return -1
    
    def remove(self, key):
        node = self.head
        while node.next:
            if node.next.key == key:
                new_next = node.next.next
                node.next = new_next
                return
            node = node.next
        
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)