# 2216 - Delete the Middle Node of a Linked List
# Date: 2022-07-11
# Runtime: 3236 ms, Memory: 60.7 MB
# Submission Id: 744359236


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        fast, slow = head.next.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head