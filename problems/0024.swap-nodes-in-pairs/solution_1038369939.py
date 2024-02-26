# 0024 - Swap Nodes in Pairs
# Date: 2023-09-02
# Runtime: 41 ms, Memory: 16.4 MB
# Submission Id: 1038369939


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
            nxt = curr.next
            
            prev.next = nxt
            curr.next = nxt.next
            nxt.next = curr
            
            prev, curr = curr, curr.next
            
        return dummy.next