# 1231 - Replace Elements with Greatest Element on Right Side
# Date: 2022-09-16
# Runtime: 276 ms, Memory: 15.1 MB
# Submission Id: 801345132


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for idx in range(len(arr)-1, -1, -1):
            arr[idx], current_max = current_max, max(current_max, arr[idx])
        return arr