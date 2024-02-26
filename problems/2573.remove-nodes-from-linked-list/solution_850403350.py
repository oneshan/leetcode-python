# 2573 - Remove Nodes From Linked List
# Date: 2022-11-27
# Runtime: 1407 ms, Memory: 61 MB
# Submission Id: 850403350


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            if stack:
                stack[-1].next = node
            stack.append(node)
            node = node.next
        return stack[0]