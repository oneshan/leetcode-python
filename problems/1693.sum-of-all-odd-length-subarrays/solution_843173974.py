# 1693 - Sum of All Odd Length Subarrays
# Date: 2022-11-14
# Runtime: 105 ms, Memory: 14 MB
# Submission Id: 843173974


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = [0] * (len(arr)+1)
        for idx in range(len(arr)):
            prefix[idx+1] += prefix[idx] + arr[idx]
        
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                ans += (prefix[j+1] - prefix[i])
        return ans