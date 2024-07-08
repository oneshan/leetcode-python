# 1306 - Minimum Absolute Difference
# Date: 2024-06-12
# Runtime: 347 ms, Memory: 45.7 MB
# Submission Id: 1285101300


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        offset = min(arr)
        buckets = [0] * (max(arr) - min(arr) + 1)
        for num in arr:
            buckets[num-offset] += 1
        
        min_diff = float('inf')
        ans = []
        prev = 0
        for curr in range(1, len(buckets)):
            if buckets[curr] == 0:
                continue
            
            if curr - prev < min_diff:
                min_diff = curr - prev
                ans = []

            if curr - prev == min_diff:
                ans.append([prev+offset, curr+offset])

            prev = curr

        return ans