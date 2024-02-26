# 0092 - Reverse Linked List II
# Date: 2023-09-07
# Runtime: 46 ms, Memory: 16.3 MB
# Submission Id: 1042577369


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        curr = dummy
        for _ in range(left-1):
            curr = curr.next
        
        def reverse(node):
            prev, curr = None, node
            for _ in range(right-left+1):
                if not curr:
                    break
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            node.next = nxt
            return prev
        
        curr.next = reverse(curr.next)
        return dummy.next