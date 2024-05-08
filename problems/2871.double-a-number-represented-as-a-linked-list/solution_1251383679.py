# 2871 - Double a Number Represented as a Linked List
# Date: 2024-05-07
# Runtime: 217 ms, Memory: 19.3 MB
# Submission Id: 1251383679


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.val > 4:
            head = ListNode(0, head)

        curr = head
        while curr:
            curr.val = (curr.val * 2) % 10
            if curr.next and curr.next.val > 4:
                curr.val += 1
            curr = curr.next
            
        return head