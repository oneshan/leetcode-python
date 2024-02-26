# 0908 - Middle of the Linked List
# Date: 2023-09-01
# Runtime: 40 ms, Memory: 16.4 MB
# Submission Id: 1037581558


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow