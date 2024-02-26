# 0816 - Design HashSet
# Date: 2022-07-15
# Runtime: 376 ms, Memory: 20.8 MB
# Submission Id: 747419625


class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.bucket = [Bucket() for i in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range
    
    def add(self, key: int) -> None:
        bucket = self.bucket[self._hash(key)]
        bucket.insert(key) 

    def remove(self, key: int) -> None:
        bucket = self.bucket[self._hash(key)]
        bucket.delete(key)

    def contains(self, key: int) -> bool:
        bucket = self.bucket[self._hash(key)]
        return bucket.exists(key)

    
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def insert(self, key):
        if self.exists(key):
            return
        self.head.next = Node(key, self.head.next)
        
    def delete(self, key):
        node = self.head
        while node.next:
            if node.next.val == key:
                new_next = node.next.next
                node.next = new_next
                return
            node = node.next
            
    def exists(self, key):
        node = self.head
        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)