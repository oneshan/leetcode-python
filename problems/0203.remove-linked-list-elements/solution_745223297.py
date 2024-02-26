# 0203 - Remove Linked List Elements
# Date: 2022-07-12
# Runtime: 136 ms, Memory: 17.8 MB
# Submission Id: 745223297


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next