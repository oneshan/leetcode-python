# 0234 - Palindrome Linked List
# Date: 2023-09-07
# Runtime: 779 ms, Memory: 132.4 MB
# Submission Id: 1043118072


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head
        
        def recur(curr):
            if curr:
                if not recur(curr.next):
                    return False
                if self.front.val != curr.val:
                    return False
                self.front = self.front.next
            return True
        
        return recur(head)