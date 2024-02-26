# 0373 - Find K Pairs with Smallest Sums
# Date: 2023-06-27
# Runtime: 1128 ms, Memory: 36.7 MB
# Submission Id: 980426208


import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        len1, len2 = len(nums1), len(nums2)
        ans = []
        seen = {(0, 0)}
        heap = [(nums1[0] + nums2[0], (0, 0))]
        
        while k and heap:
            val, (p1, p2) = heapq.heappop(heap)
            ans.append([nums1[p1], nums2[p2]])
            if p1 < len1 - 1 and (p1+1, p2) not in seen:
                heappush(heap, (nums1[p1+1] + nums2[p2], (p1+1, p2)))
                seen.add((p1+1, p2))
            if p2 < len2 - 1 and (p1, p2+1) not in seen:
                heappush(heap, (nums1[p1] + nums2[p2+1], (p1, p2+1)))
                seen.add((p1, p2+1))
            k -= 1
    
        return ans