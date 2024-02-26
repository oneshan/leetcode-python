# 1956 - Maximum Element After Decreasing and Rearranging
# Date: 2023-11-15
# Runtime: 423 ms, Memory: 26.3 MB
# Submission Id: 1099425331


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1
        return ans