# 0445 - Add Two Numbers II
# Date: 2023-07-17
# Runtime: 80 ms, Memory: 16.4 MB
# Submission Id: 996331676


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(curr):
            prev = temp = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        curr = ListNode()
        total = 0
        while l1 or l2:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            curr.val = total % 10
            total //= 10
            curr = ListNode(total, curr)
            
        return curr.next if curr.val == 0 else curr