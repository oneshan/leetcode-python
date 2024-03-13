# 1267 - Remove Zero Sum Consecutive Nodes from Linked List
# Date: 2024-03-12
# Runtime: 42 ms, Memory: 16.8 MB
# Submission Id: 1201127423


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        seen = {}

        prefix = 0
        curr = dummy
        while curr:
            prefix += curr.val

            if prefix not in seen:
                seen[prefix] = curr
            else:
                prev = seen[prefix]
                curr = prev.next
                temp = prefix + curr.val
                while temp != prefix:
                    seen.pop(temp)
                    curr = curr.next
                    temp += curr.val
                prev.next = curr.next

            curr = curr.next
        
        return dummy.next