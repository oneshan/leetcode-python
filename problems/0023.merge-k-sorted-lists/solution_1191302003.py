# 0023 - Merge k Sorted Lists
# Date: 2024-03-02
# Runtime: 87 ms, Memory: 20 MB
# Submission Id: 1191302003


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        heap = [(lists[i].val, i) for i in range(n) if lists[i]]
        heapq.heapify(heap)
        
        head = curr = ListNode()
        while heap:
            _, i = heapq.heappop(heap)
            curr.next = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
            curr = curr.next

        return head.next