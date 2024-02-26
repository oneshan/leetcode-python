# 0528 - Swapping Nodes in a Linked List
# Date: 2023-09-07
# Runtime: 719 ms, Memory: 50.8 MB
# Submission Id: 1042604015


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        fast = slow = dummy
        for _ in range(k-1):
            fast = fast.next
        prev1 = fast
        
        fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        prev2 = slow

        # swap node
        prev1.next, prev2.next = prev2.next, prev1.next
        prev1.next.next, prev2.next.next = prev2.next.next, prev1.next.next
        
        return dummy.next