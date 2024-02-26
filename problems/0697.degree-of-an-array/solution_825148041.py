# 0697 - Degree of an Array
# Date: 2022-10-18
# Runtime: 369 ms, Memory: 15.4 MB
# Submission Id: 825148041


from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        first_pos = {}
        ans = degree = 0
        for idx, num in enumerate(nums):
            counter[num] += 1
            if num not in first_pos:
                first_pos[num] = idx
            if counter[num] > degree:
                degree = counter[num]
                ans = idx - first_pos[num] + 1
            elif counter[num] == degree:
                ans = min(ans, idx - first_pos[num] + 1)
        return ans