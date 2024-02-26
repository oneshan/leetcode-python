# 0237 - Delete Node in a Linked List
# Date: 2022-07-11
# Runtime: 71 ms, Memory: 14.3 MB
# Submission Id: 744372460


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next