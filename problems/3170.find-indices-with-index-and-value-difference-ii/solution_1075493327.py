# 3170 - Find Indices With Index and Value Difference II
# Date: 2023-10-15
# Runtime: 732 ms, Memory: 31.2 MB
# Submission Id: 1075493327


from collections import deque

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        
        if indexDifference == 0 and valueDifference == 0:
            return [0, 0]
        
        curr_min = [i for i in range(n)]
        curr_max = [i for i in range(n)]
        for i in range(1, n):
            curr_min[i] = i if nums[i] < nums[curr_min[i-1]] else curr_min[i-1]
            curr_max[i] = i if nums[i] > nums[curr_max[i-1]] else curr_max[i-1]
            if i >= indexDifference:
                if nums[i] - nums[curr_min[i-indexDifference]] >= valueDifference:
                    return [curr_min[i-indexDifference], i]
                if nums[curr_max[i-indexDifference]] - nums[i] >= valueDifference:
                    return [curr_max[i-indexDifference], i]
        return [-1, -1]