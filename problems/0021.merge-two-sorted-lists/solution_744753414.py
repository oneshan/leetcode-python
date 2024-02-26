# 0021 - Merge Two Sorted Lists
# Date: 2022-07-12
# Runtime: 53 ms, Memory: 14 MB
# Submission Id: 744753414


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        node = dummy
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1:
            node.next = list1
        else:
            node.next = list2
        return dummy.next