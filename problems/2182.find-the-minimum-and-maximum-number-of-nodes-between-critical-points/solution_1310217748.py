# 2182 - Find the Minimum and Maximum Number of Nodes Between Critical Points
# Date: 2024-07-05
# Runtime: 369 ms, Memory: 44.5 MB
# Submission Id: 1310217748


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev, curr = head, head.next
        idx = 1
        
        first_pt = prev_pt = None
        max_dist, min_dist = -1, float('inf')

        while curr and curr.next:
            if prev.val < curr.val > curr.next.val or prev.val > curr.val < curr.next.val:
                if first_pt is None:
                    first_pt = prev_pt = idx
                else:
                    min_dist = min(min_dist, idx - prev_pt)
                    prev_pt = idx
            prev, curr = curr, curr.next
            idx += 1

        if min_dist == float('inf'):
            return [-1, -1]
        max_dist = prev_pt - first_pt
        return [min_dist, max_dist]