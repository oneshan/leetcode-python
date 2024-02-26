# 0147 - Insertion Sort List
# Date: 2023-10-06
# Runtime: 1310 ms, Memory: 18.9 MB
# Submission Id: 1068605593


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        while head:
            prev = dummy
            while prev.next and prev.next.val <= head.val:
                prev = prev.next
            
            temp = head.next
            head.next = prev.next
            prev.next = head
            head = temp
            
        return dummy.next