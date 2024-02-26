# 3226 - Minimum Number Game
# Date: 2023-12-24
# Runtime: 52 ms, Memory: 17.4 MB
# Submission Id: 1127029547


import heapq

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        heapq.heapify(nums)
        while nums:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            ans.append(bob)
            ans.append(alice)
        return ans