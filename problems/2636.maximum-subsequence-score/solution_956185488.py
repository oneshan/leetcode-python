# 2636 - Maximum Subsequence Score
# Date: 2023-05-24
# Runtime: 1025 ms, Memory: 37.9 MB
# Submission Id: 956185488


import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = [(n2, n1) for n1, n2 in zip(nums1, nums2)]
        pairs.sort(reverse=True)
        
        heap, total = [], 0
        for i in range(k):
            heapq.heappush(heap, pairs[i][1])
            total += pairs[i][1]
        ans = total * pairs[k-1][0]
        
        for i in range(k, n):
            total -= heapq.heappop(heap)
            total += pairs[i][1]
            heapq.heappush(heap, pairs[i][1])
            ans = max(ans, total * pairs[i][0])
        
        return ans