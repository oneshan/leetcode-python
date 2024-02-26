# 0786 - Search in a Sorted Array of Unknown Size
# Date: 2022-10-10
# Runtime: 41 ms, Memory: 15.2 MB
# Submission Id: 819317470


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0
        
        # find boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left, right = right, right<<1
         
        # binary search
        while left <= right:
            mid = (left + right) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            if val > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1