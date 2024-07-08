# 0373 - Find K Pairs with Smallest Sums
# Date: 2024-06-16
# Runtime: 957 ms, Memory: 36.1 MB
# Submission Id: 1290187245


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        seen = {(0, 0)}

        ans = []
        for _ in range(k):
            val, idx1, idx2 = heapq.heappop(heap)
            ans.append([nums1[idx1], nums2[idx2]])
            if idx1 + 1 < len(nums1) and (idx1+1, idx2) not in seen:
                seen.add((idx1+1, idx2))
                heapq.heappush(heap, (nums1[idx1+1] + nums2[idx2], idx1+1, idx2))
            
            if idx2 + 1 < len(nums2) and (idx1, idx2+1) not in seen:
                seen.add((idx1, idx2+1))
                heapq.heappush(heap, (nums1[idx1] + nums2[idx2+1], idx1, idx2+1))

        return ans