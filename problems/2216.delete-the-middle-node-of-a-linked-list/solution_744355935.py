# 2216 - Delete the Middle Node of a Linked List
# Date: 2022-07-11
# Runtime: 3405 ms, Memory: 60.3 MB
# Submission Id: 744355935


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        fast, slow = head, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return dummy.next