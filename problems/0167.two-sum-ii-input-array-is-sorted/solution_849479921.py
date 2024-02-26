# 0167 - Two Sum II - Input Array Is Sorted
# Date: 2022-11-25
# Runtime: 454 ms, Memory: 14.9 MB
# Submission Id: 849479921


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            if total > target:
                right -= 1
            else:
                left += 1