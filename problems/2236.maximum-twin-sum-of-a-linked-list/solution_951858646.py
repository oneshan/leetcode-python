# 2236 - Maximum Twin Sum of a Linked List
# Date: 2023-05-17
# Runtime: 852 ms, Memory: 47.5 MB
# Submission Id: 951858646


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # find middle node
        p1 = p2 = head
        while p1 and p1.next:
            p1, p2 = p1.next.next, p2.next
            
        # reverse
        prev, curr = None, p2
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        ans = 0
        p1, p2 = head, prev
        while p2:
            ans = max(ans, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        return ans