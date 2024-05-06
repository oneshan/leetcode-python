# 1231 - Replace Elements with Greatest Element on Right Side
# Date: 2024-05-05
# Runtime: 516 ms, Memory: 19 MB
# Submission Id: 1249852824


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n

        curr = arr[-1]
        for i in range(n-2, -1, -1):
            ans[i] = curr
            curr = max(curr, arr[i])
        return ans