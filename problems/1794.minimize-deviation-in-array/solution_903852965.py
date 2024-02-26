# 1794 - Minimize Deviation in Array
# Date: 2023-02-24
# Runtime: 2132 ms, Memory: 21.5 MB
# Submission Id: 903852965


import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        minimum = float('inf')
        for num in nums:
            num = num<<1 if num & 1 else num
            minimum = min(minimum, num)
            heapq.heappush(heap, -num)
            
        ans = float('inf')
        while heap:
            num = -heapq.heappop(heap)
            ans = min(ans, num-minimum)
            if num & 1:
                break
            num >>= 1
            minimum = min(minimum, num)
            heapq.heappush(heap, -num)
        return ans