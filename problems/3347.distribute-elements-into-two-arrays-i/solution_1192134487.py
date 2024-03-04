# 3347 - Distribute Elements Into Two Arrays I
# Date: 2024-03-03
# Runtime: 43 ms, Memory: 16.6 MB
# Submission Id: 1192134487


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2