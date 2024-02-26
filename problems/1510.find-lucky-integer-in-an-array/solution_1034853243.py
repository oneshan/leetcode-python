# 1510 - Find Lucky Integer in an Array
# Date: 2023-08-29
# Runtime: 64 ms, Memory: 16.2 MB
# Submission Id: 1034853243


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        
        n = len(arr)
        count = 0
        for idx, num in enumerate(arr):
            count += 1
            if idx == n-1 or num != arr[idx+1]:
                if arr[idx] == count:
                    return num
                count = 0
        return -1