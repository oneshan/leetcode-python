# 0445 - Add Two Numbers II
# Date: 2023-07-17
# Runtime: 91 ms, Memory: 16.4 MB
# Submission Id: 996329412


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        total_sum = 0
        curr = ListNode()
        while stack1 or stack2:
            if stack1:
                total_sum += stack1.pop()
            if stack2:
                total_sum += stack2.pop()
            
            curr.val = total_sum % 10
            carry = total_sum // 10
            curr = ListNode(carry, curr)
            total_sum = carry

        return curr.next if curr.val == 0 else curr