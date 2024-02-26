# 0347 - Top K Frequent Elements
# Date: 2022-07-19
# Runtime: 113 ms, Memory: 19.7 MB
# Submission Id: 751139346


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in counter.items():
            bucket[freq].append(num)
        
        ans = []
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                ans.extend(bucket[i])
            if len(ans) > k:
                break
        return ans[:k]