# 0142 - Linked List Cycle II
# Date: 2022-07-12
# Runtime: 97 ms, Memory: 17.9 MB
# Submission Id: 745059831


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None