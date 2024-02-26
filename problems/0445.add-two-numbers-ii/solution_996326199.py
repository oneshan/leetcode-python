# 0445 - Add Two Numbers II
# Date: 2023-07-17
# Runtime: 94 ms, Memory: 16.3 MB
# Submission Id: 996326199


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        len1, len2 = 0, 0
        while p1 or p2:
            if p1:
                p1, len1 = p1.next, len1 + 1
            if p2:
                p2, len2 = p2.next, len2 + 1

        dummy = ListNode(0)
        curr = dummy
        size = max(len1, len2)
        while size:
            val = 0
            if size <= len1:
                val += l1.val
                l1 = l1.next
            if size <= len2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val)
            curr = curr.next
            size -= 1

        prev = dummy
        while prev:
            curr = prev.next
            while curr and curr.val == 9:
                curr = curr.next
            while prev != curr:
                if curr and curr.val > 9:
                    prev.val += 1
                    prev.next.val -= 10
                prev = prev.next

        return dummy if dummy.val else dummy.next