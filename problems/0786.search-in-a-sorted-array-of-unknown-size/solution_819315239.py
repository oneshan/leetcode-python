# 0786 - Search in a Sorted Array of Unknown Size
# Date: 2022-10-10
# Runtime: 74 ms, Memory: 15.2 MB
# Submission Id: 819315239


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 2**31-1
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