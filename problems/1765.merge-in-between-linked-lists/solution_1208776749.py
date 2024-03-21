# 1765 - Merge In Between Linked Lists
# Date: 2024-03-20
# Runtime: 189 ms, Memory: 21 MB
# Submission Id: 1208776749


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        curr = list1
        for _ in range(a-1):
            curr = curr.next
        
        merge_head = curr
        for _ in range(b-a+1):
            curr = curr.next
        merge_head.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = curr.next

        return list1