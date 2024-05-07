# 2573 - Remove Nodes From Linked List
# Date: 2024-05-06
# Runtime: 415 ms, Memory: 51.5 MB
# Submission Id: 1250526035


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next

        for i in range(len(stack)-1):
            stack[i].next = stack[i+1]
        stack[-1].next = None

        return stack[0]