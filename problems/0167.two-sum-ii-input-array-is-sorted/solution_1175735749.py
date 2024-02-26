# 0167 - Two Sum II - Input Array Is Sorted
# Date: 2024-02-15
# Runtime: 113 ms, Memory: 17.4 MB
# Submission Id: 1175735749


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            if total < target:
                left += 1
            else:
                right -= 1