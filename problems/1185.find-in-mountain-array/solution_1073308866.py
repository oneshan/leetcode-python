# 1185 - Find in Mountain Array
# Date: 2023-10-12
# Runtime: 38 ms, Memory: 17 MB
# Submission Id: 1073308866


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
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                right = mid
            else:
                left = mid + 1
        
        left, right = peak_idx, n
        while left < right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val < target:
                right = mid
            else:
                left = mid + 1
        return -1