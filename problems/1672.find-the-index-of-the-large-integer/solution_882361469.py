# 1672 - Find the Index of the Large Integer
# Date: 2023-01-21
# Runtime: 278 ms, Memory: 53 MB
# Submission Id: 882361469


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1
        while left < right:
            mid_1 = (left + right) // 2
            mid_2 = (left + right + 1) // 2
            if reader.compareSub(left, mid_1, mid_2, right) < 0:
                left = mid_2
            else:
                right = mid_1
        return left