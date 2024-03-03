# 0148 - Sort List
# Date: 2024-03-02
# Runtime: 239 ms, Memory: 37.1 MB
# Submission Id: 1191297247


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        heap = []
        i = 0
        while head:
            heapq.heappush(heap, (head.val, i, head))
            i += 1
            head = head.next
        
        new_head = curr = ListNode()
        while heap:
            _, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
        curr.next = None
        return new_head.next