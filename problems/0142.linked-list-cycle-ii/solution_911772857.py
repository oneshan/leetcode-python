# 0142 - Linked List Cycle II
# Date: 2023-03-09
# Runtime: 42 ms, Memory: 17.4 MB
# Submission Id: 911772857


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return fast