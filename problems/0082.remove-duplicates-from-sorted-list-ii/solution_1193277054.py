# 0082 - Remove Duplicates from Sorted List II
# Date: 2024-03-04
# Runtime: 38 ms, Memory: 16.8 MB
# Submission Id: 1193277054


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev, curr = dummy, head
        while curr:
            if curr.next and curr.next.val == curr.val:
                value = curr.val
                while curr and curr.val == value:
                    curr = curr.next
            else:
                prev.next = curr
                prev, curr = curr, curr.next
        
        prev.next = None
        return dummy.next           