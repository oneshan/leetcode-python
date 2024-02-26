# 0203 - Remove Linked List Elements
# Date: 2023-09-07
# Runtime: 69 ms, Memory: 19.8 MB
# Submission Id: 1043128294


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head if head.val != val else head.next