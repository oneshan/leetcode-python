# 0237 - Delete Node in a Linked List
# Date: 2024-05-05
# Runtime: 36 ms, Memory: 16.9 MB
# Submission Id: 1249756093


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