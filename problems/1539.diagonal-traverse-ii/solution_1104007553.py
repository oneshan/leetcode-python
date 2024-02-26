# 1539 - Diagonal Traverse II
# Date: 2023-11-22
# Runtime: 801 ms, Memory: 38.6 MB
# Submission Id: 1104007553


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        new_arr = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                new_arr.append((i+j, -i, nums[i][j]))
        return [num for _, _, num in sorted(new_arr)]