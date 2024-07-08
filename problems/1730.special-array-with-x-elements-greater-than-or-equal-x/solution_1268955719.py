# 1730 - Special Array With X Elements Greater Than or Equal X
# Date: 2024-05-27
# Runtime: 42 ms, Memory: 16.4 MB
# Submission Id: 1268955719


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        buckets = [0] * 1001
        for num in nums:
            buckets[num] += 1
        
        curr = 0
        for i in range(1000, -1, -1):
            curr += buckets[i]
            if curr == i:
                return i
        return -1