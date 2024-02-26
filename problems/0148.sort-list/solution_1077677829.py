# 0148 - Sort List
# Date: 2023-10-18
# Runtime: 475 ms, Memory: 38.6 MB
# Submission Id: 1077677829


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def get_mid(self, head):
        if not head or not head.next:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, left, right):
        curr = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        return dummy.next