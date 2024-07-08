# 1982 - Remove Duplicates From an Unsorted Linked List
# Date: 2024-07-08
# Runtime: 528 ms, Memory: 47 MB
# Submission Id: 1313866724


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        seen = set()
        to_delete = set()

        curr = head
        while curr:
            if curr.val in seen:
                to_delete.add(curr.val)
            seen.add(curr.val)
            curr = curr.next
        
        curr = dummy
        while curr.next:
            if curr.next.val in to_delete:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
