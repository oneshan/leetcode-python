# 1693 - Sum of All Odd Length Subarrays
# Date: 2022-11-14
# Runtime: 55 ms, Memory: 13.9 MB
# Submission Id: 843175131


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        
        ans = 0
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                if (j-i+1) & 1:
                    ans += curr_sum
        return ans