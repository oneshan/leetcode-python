# 1693 - Sum of All Odd Length Subarrays
# Date: 2022-11-14
# Runtime: 71 ms, Memory: 14 MB
# Submission Id: 843180251


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        
        for idx, num in enumerate(arr):
            left, right = idx, n-idx-1
            odd_left = (left >> 1) + 1
            odd_right = (right >> 1) + 1
            even_left = (left + 1) >> 1
            even_right = (right + 1) >> 1
            ans += num * (odd_left * odd_right)
            ans += num * (even_left * even_right)

        return ans