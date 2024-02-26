# 0167 - Two Sum II - Input Array Is Sorted
# Date: 2023-10-29
# Runtime: 188 ms, Memory: 17.2 MB
# Submission Id: 1086774593


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            left, right = i+1, n-1
            while left <= right:
                mid = (left + right) // 2
                two_sum = numbers[i] + numbers[mid]
                if two_sum == target:
                    return [i+1, mid+1]
                if two_sum < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return [-1, -1]