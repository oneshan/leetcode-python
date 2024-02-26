# 0234 - Palindrome Linked List
# Date: 2022-09-26
# Runtime: 792 ms, Memory: 39.1 MB
# Submission Id: 808375206


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow.next == Middle
        
        # Reverse from Middle
        prev, curr = None, slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        slow.next = None
        
        p1, p2 = head, prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True