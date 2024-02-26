# 2216 - Delete the Middle Node of a Linked List
# Date: 2023-09-01
# Runtime: 1225 ms, Memory: 62.9 MB
# Submission Id: 1037602072


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        fast, slow = head, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return dummy.next