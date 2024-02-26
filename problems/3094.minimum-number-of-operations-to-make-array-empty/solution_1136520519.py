# 3094 - Minimum Number of Operations to Make Array Empty
# Date: 2024-01-04
# Runtime: 541 ms, Memory: 31.3 MB
# Submission Id: 1136520519


from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        ans = 0
        for count in counter.values():
            if count < 2:
                return -1
            ans += (count // 3) + (count % 3 != 0)
        return ans