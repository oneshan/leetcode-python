# 0019 - Remove Nth Node From End of List
# Date: 2022-07-12
# Runtime: 57 ms, Memory: 13.9 MB
# Submission Id: 745210002


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size, node = 0, head
        while node:
            node = node.next
            size += 1
        
        dummy = ListNode(0, head)
        node = dummy
        for _ in range(size-n):
            node = node.next
        node.next = node.next.next
        return dummy.next