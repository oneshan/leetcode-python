# 0025 - Reverse Nodes in k-Group
# Date: 2024-05-24
# Runtime: 43 ms, Memory: 17.4 MB
# Submission Id: 1266606988


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def get_kth(node):
            for _ in range(k-1):
                node = node.next
                if not node:
                    return None
            return node

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
            tail = get_kth(head)
            if not tail:
                curr.next = head
                break
            next_head = tail.next
            tail.next = None

            curr.next = reverse(head)
            curr, head = head, next_head

        return dummy.next

        