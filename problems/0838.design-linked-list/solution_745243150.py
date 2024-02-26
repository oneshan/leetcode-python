# 0838 - Design Linked List
# Date: 2022-07-12
# Runtime: 142 ms, Memory: 15.4 MB
# Submission Id: 745243150


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

        
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        node = self.head
        for _ in range(index + 1):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        prev, next = self.head, self.head.next
        node = ListNode(val)
        prev.next = next.prev = node
        node.prev = prev
        node.next = next
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        prev, next = self.tail.prev, self.tail        
        node = ListNode(val)
        prev.next = next.prev = node
        node.prev = prev
        node.next = next
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next
        next = prev.next
        
        node = ListNode(val)
        prev.next = next.prev = node
        node.prev = prev
        node.next = next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next
        next = prev.next.next
        
        prev.next = next
        next.prev = prev
        self.size -= 1        
