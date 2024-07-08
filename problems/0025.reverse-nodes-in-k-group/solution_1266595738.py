# 0025 - Reverse Nodes in k-Group
# Date: 2024-05-24
# Runtime: 43 ms, Memory: 17.3 MB
# Submission Id: 1266595738


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def pass_k(node):
            prev, curr = node, node.next
            for _ in range(k-1):
                if not curr:
                    return None, None
                prev = prev.next
                curr = curr.next
            return prev, curr

        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            return prev

        dummy = ListNode(0, head)
        curr = dummy
        while head:
            tail, next_head = pass_k(head)
            if not tail:
                curr.next = head
                break
            tail.next = None
            curr.next = reverse(head)
            curr = head
            head = next_head
        return dummy.next

        