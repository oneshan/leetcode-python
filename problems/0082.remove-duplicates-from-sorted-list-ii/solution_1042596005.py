# 0082 - Remove Duplicates from Sorted List II
# Date: 2023-09-07
# Runtime: 46 ms, Memory: 16.5 MB
# Submission Id: 1042596005


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                skip = curr.val
                while curr and curr.val == skip:
                    curr = curr.next
            else:
                prev.next = curr
                curr, prev = curr.next, curr
                
        prev.next = None
        return dummy.next