# 0838 - Design Linked List
# Date: 2023-09-07
# Runtime: 124 ms, Memory: 17.8 MB
# Submission Id: 1043154670


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.tail = self.head = ListNode(0)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.size += 1
        node = ListNode(val)
        
        nxt = self.head.next
        node.prev, node.next = self.head, nxt
        self.head.next = nxt.prev = node

    def addAtTail(self, val: int) -> None:
        self.size += 1
        node = ListNode(val)
        
        prev = self.tail.prev
        node.prev = prev
        node.next = self.tail
        prev.next = self.tail.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        curr = self.head
        for _ in range(index):
            curr = curr.next        
        nxt = curr.next
        
        self.size += 1
        node = ListNode(val)
        curr.next = nxt.prev = node
        node.prev = curr
        node.next = nxt
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head
        for _ in range(index):
            curr = curr.next        
        nxt = curr.next.next
        
        self.size -= 1
        curr.next = nxt
        nxt.prev = curr    
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)