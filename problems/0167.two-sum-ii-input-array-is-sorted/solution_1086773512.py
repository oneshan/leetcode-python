# 0167 - Two Sum II - Input Array Is Sorted
# Date: 2023-10-29
# Runtime: 129 ms, Memory: 17.3 MB
# Submission Id: 1086773512


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left + 1, right + 1]
            if two_sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]