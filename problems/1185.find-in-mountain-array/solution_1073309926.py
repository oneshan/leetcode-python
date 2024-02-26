# 1185 - Find in Mountain Array
# Date: 2023-10-12
# Runtime: 31 ms, Memory: 17.1 MB
# Submission Id: 1073309926


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        left, right = 1, n-2
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                right = mid
            else:
                left = mid + 1
        peak_idx = left
        
        left, right = 0, peak_idx
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
                
        if mountain_arr.get(left) == target:
            return left
        
        left, right = peak_idx + 1, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) <= target:
                right = mid
            else:
                left = mid + 1
                
        if mountain_arr.get(left) == target:
            return left

        return -1