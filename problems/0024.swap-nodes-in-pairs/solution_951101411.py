# 0024 - Swap Nodes in Pairs
# Date: 2023-05-16
# Runtime: 42 ms, Memory: 16.2 MB
# Submission Id: 951101411


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        prev, curr = dummy, head
        while curr and curr.next:
            p1, p2 = curr, curr.next
            prev.next, p1.next, p2.next = p2, p2.next, p1
            
            prev, curr = curr, curr.next
        return dummy.next