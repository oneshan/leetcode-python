# 2117 - Find Original Array From Doubled Array
# Date: 2023-09-14
# Runtime: 1123 ms, Memory: 32 MB
# Submission Id: 1048563887


import heapq

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        heap = []
        ans = []
        
        for x in sorted(changed):
            if heap and x == heap[0] * 2:
                ans.append(heapq.heappop(heap))
            else:
                heapq.heappush(heap, x)
        return ans if not heap else []