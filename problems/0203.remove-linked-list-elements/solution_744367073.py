# 0203 - Remove Linked List Elements
# Date: 2022-07-11
# Runtime: 120 ms, Memory: 17.7 MB
# Submission Id: 744367073


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        tmp = dummy
        while tmp:
            while tmp.next and tmp.next.val == val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return dummy.next