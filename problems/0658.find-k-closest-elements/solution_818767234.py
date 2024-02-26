# 0658 - Find K Closest Elements
# Date: 2022-10-10
# Runtime: 777 ms, Memory: 15.4 MB
# Submission Id: 818767234


import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(num-x))
        return sorted(sorted_arr[:k])