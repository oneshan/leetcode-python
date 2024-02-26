# 1693 - Sum of All Odd Length Subarrays
# Date: 2022-11-14
# Runtime: 33 ms, Memory: 13.9 MB
# Submission Id: 843250158


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, n = 0, len(arr)
        for idx, num in enumerate(arr):
            # start with arr[idx]: (n-idx)
            # non-start with arr[idx]: idx * (n-idx)
            total = idx * (n-idx) + (n-idx)
            odd_count = (total + 1) // 2
            ans += num * odd_count
        return ans