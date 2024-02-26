# 0141 - Linked List Cycle
# Date: 2022-09-25
# Runtime: 116 ms, Memory: 17.6 MB
# Submission Id: 808145944


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
            