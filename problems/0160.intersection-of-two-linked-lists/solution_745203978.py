# 0160 - Intersection of Two Linked Lists
# Date: 2022-07-12
# Runtime: 161 ms, Memory: 29.6 MB
# Submission Id: 745203978


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_1, node_2 = headA, headB
        while node_1 != node_2:
            node_1 = node_1.next if node_1 else headB
            node_2 = node_2.next if node_2 else headA
        return node_1