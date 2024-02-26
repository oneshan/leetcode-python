# 0019 - Remove Nth Node From End of List
# Date: 2023-09-01
# Runtime: 33 ms, Memory: 16.3 MB
# Submission Id: 1037603326


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        slow, fast = dummy, head
        for _ in range(n):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next