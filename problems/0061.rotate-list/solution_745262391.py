# 0061 - Rotate List
# Date: 2022-07-12
# Runtime: 89 ms, Memory: 13.8 MB
# Submission Id: 745262391


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        dummy = ListNode(0, head)
        node, size = dummy, 0
        while node.next:
            node = node.next
            size += 1
        
        k = (k-1) % size + 1
        
        p1, p2 = dummy, dummy
        for _ in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        # Rotate
        if p1 != dummy:
            dummy.next = p1.next
            p1.next = None
            p2.next = head

        return dummy.next
