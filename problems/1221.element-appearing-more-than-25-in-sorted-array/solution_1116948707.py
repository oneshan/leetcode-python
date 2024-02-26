# 1221 - Element Appearing More Than 25% In Sorted Array
# Date: 2023-12-11
# Runtime: 81 ms, Memory: 17.6 MB
# Submission Id: 1116948707


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n//4], arr[n//2], arr[-n//4]]
        
        for num in candidates:
            left = bisect_left(arr, num)
            right = bisect_right(arr, num) - 1
            if right - left + 1 > n / 4:
                return num
        return -1