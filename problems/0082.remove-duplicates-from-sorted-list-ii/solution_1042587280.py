# 0082 - Remove Duplicates from Sorted List II
# Date: 2023-09-07
# Runtime: 41 ms, Memory: 16.4 MB
# Submission Id: 1042587280


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = head

            head = head.next            

        return dummy.next