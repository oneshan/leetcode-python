# 0948 - Sort an Array
# Date: 2023-03-01
# Runtime: 813 ms, Memory: 22.2 MB
# Submission Id: 907101260


import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = []
        while nums:
            ans.append(heapq.heappop(nums))
        return ans