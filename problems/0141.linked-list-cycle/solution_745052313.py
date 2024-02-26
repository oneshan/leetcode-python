# 0141 - Linked List Cycle
# Date: 2022-07-12
# Runtime: 85 ms, Memory: 17.9 MB
# Submission Id: 745052313


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False