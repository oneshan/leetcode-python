# 0908 - Middle of the Linked List
# Date: 2022-07-13
# Runtime: 50 ms, Memory: 13.9 MB
# Submission Id: 745624467


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow