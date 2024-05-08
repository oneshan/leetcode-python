# 0948 - Sort an Array
# Date: 2024-05-07
# Runtime: 572 ms, Memory: 27 MB
# Submission Id: 1251500684


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