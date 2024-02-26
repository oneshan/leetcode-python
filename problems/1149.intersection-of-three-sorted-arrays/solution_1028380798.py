# 1149 - Intersection of Three Sorted Arrays
# Date: 2023-08-22
# Runtime: 67 ms, Memory: 16.7 MB
# Submission Id: 1028380798


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1) & set(arr2) & set(arr3))