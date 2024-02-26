# 1221 - Element Appearing More Than 25% In Sorted Array
# Date: 2023-12-11
# Runtime: 89 ms, Memory: 17.7 MB
# Submission Id: 1116947480


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        size = n // 4
        for i in range(n-size):
            if arr[i] == arr[i+size]:
                return arr[i]
        return -1