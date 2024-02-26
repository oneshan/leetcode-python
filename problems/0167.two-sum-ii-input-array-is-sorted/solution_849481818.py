# 0167 - Two Sum II - Input Array Is Sorted
# Date: 2022-11-25
# Runtime: 732 ms, Memory: 14.9 MB
# Submission Id: 849481818


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for idx in range(n):
            left, right = idx+1, n-1
            while left <= right:
                mid = (left + right) // 2
                two_sum = numbers[idx] + numbers[mid]
                if two_sum == target:
                    return [idx+1, mid+1]
                if two_sum > target:
                    right = mid - 1
                else:
                    left = mid + 1