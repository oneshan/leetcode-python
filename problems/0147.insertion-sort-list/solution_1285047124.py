# 0147 - Insertion Sort List
# Date: 2024-06-11
# Runtime: 78 ms, Memory: 18.7 MB
# Submission Id: 1285047124


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(-5000, head)        
        last_sorted = head
        curr = head.next

        while curr:

            if curr.val >= last_sorted.val:
                last_sorted = curr
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            curr = last_sorted.next
            
        return dummy.next