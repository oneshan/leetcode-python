# 1765 - Merge In Between Linked Lists
# Date: 2022-12-01
# Runtime: 610 ms, Memory: 20.5 MB
# Submission Id: 852701717


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        for _ in range(a-1):
            node = node.next
        
        remove = node.next
        for _ in range(b-a):
            remove = remove.next    
        
        node.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = remove.next
        
        return list1