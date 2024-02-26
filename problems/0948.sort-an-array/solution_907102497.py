# 0948 - Sort an Array
# Date: 2023-03-01
# Runtime: 794 ms, Memory: 24 MB
# Submission Id: 907102497


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [0] * 100001
        for num in nums:
            bucket[num+50000] += 1
        
        ans = []
        for i in range(100001):
            if bucket[i]:
                ans += [i-50000] * bucket[i]
        return ans