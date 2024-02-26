# 2236 - Maximum Twin Sum of a Linked List
# Date: 2022-09-26
# Runtime: 1214 ms, Memory: 45 MB
# Submission Id: 809082925


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        # find middle node (slow)
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half list, new head is prev
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        # twim sum
        ans = float('-inf')
        fast = head
        while prev:
            ans = max(ans, fast.val + prev.val)
            fast = fast.next
            prev = prev.next
        
        return ans