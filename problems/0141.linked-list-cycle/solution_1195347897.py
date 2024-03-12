# 0141 - Linked List Cycle
# Date: 2024-03-06
# Runtime: 41 ms, Memory: 19 MB
# Submission Id: 1195347897


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False