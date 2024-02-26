# 0978 - Valid Mountain Array
# Date: 2022-09-15
# Runtime: 449 ms, Memory: 15.4 MB
# Submission Id: 800435250


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        idx = 0
        while idx+1 < n and arr[idx] < arr[idx+1]:
            idx += 1
        
        if idx == 0 or idx == n-1:  # [3,2,1] or [1,2,3]
            return False
        
        while idx+1 < n and arr[idx] > arr[idx+1]:
            idx += 1

        return idx == n - 1