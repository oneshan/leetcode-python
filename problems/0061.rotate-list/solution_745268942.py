# 0061 - Rotate List
# Date: 2022-07-12
# Runtime: 42 ms, Memory: 13.8 MB
# Submission Id: 745268942


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # build cycle
        node, size = head, 1
        while node.next:
            node = node.next
            size += 1
        node.next = head
                
        node = head
        for _ in range(size - k % size - 1):
            node = node.next
            
        new_head = node.next
        node.next = None
        return new_head