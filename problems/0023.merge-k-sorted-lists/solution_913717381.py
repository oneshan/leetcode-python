# 0023 - Merge k Sorted Lists
# Date: 2023-03-12
# Runtime: 106 ms, Memory: 17.9 MB
# Submission Id: 913717381


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, idx))
        
        dummy = ListNode()
        curr = dummy
        while heap:
            _, idx = heapq.heappop(heap)
            node = lists[idx]
            curr.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, idx))
            lists[idx] = lists[idx].next
            curr = curr.next
        return dummy.next