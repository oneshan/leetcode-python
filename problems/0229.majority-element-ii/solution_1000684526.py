# 0229 - Majority Element II
# Date: 2023-07-22
# Runtime: 128 ms, Memory: 17.8 MB
# Submission Id: 1000684526


from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n / 3
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        return [num for num in freq if freq[num] > target]