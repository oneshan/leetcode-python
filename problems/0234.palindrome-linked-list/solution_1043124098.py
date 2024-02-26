# 0234 - Palindrome Linked List
# Date: 2023-09-07
# Runtime: 569 ms, Memory: 41.4 MB
# Submission Id: 1043124098


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0, head)
        
        fast, slow = head, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # midddle = slow.next
        
        # reverse slow > end
        prev, curr = None, slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        slow.next = None
        
        # check palindrome
        p1, p2 = head, prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True