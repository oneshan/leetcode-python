# 0658 - Find K Closest Elements
# Date: 2023-09-17
# Runtime: 246 ms, Memory: 17.8 MB
# Submission Id: 1051063988


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left+k]