# 1168 - Duplicate Zeros
# Date: 2022-09-15
# Runtime: 117 ms, Memory: 14.7 MB
# Submission Id: 800413404


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero = sum(num == 0 for num in arr)
        if zero == 0:
            return
        
        n = len(arr)
        for idx in range(n-1, -1, -1):
            if idx + zero < n:
                arr[idx + zero] = arr[idx]
            if arr[idx] == 0:
                zero -= 1
                if idx + zero < n:
                    arr[idx + zero] = arr[idx]