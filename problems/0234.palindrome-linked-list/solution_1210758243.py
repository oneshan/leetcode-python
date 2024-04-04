# 0234 - Palindrome Linked List
# Date: 2024-03-22
# Runtime: 267 ms, Memory: 32 MB
# Submission Id: 1210758243


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # find middle
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next

        # reverse
        prev, curr = None, p2
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        p1, p2 = head, prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True