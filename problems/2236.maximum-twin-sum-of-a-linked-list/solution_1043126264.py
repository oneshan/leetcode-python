# 2236 - Maximum Twin Sum of a Linked List
# Date: 2023-09-07
# Runtime: 675 ms, Memory: 47.3 MB
# Submission Id: 1043126264


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
        p1, p2 = head, prev
        while p2:
            ans = max(ans, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        
        return ans