# 3290 - Number of Subarrays That Match a Pattern II
# Date: 2024-02-11
# Runtime: 1501 ms, Memory: 61.4 MB
# Submission Id: 1171875286


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        
        arr = []
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if diff == 0:
                arr.append(0)
            elif diff < 0:
                arr.append(-1)
            else:
                arr.append(1)
        
        len_s, len_p = len(arr), len(pattern)
        res = 0
        lps = [0] * len_p

        # compute prefix
        j = 0
        for i in range(1, len_p):
            while j and pattern[i] != pattern[j]:
                j = lps[j-1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        # find pattern
        j = 0
        for i in range(len_s):
            while j and arr[i] != pattern[j]:
                j = lps[j-1]
            if arr[i] == pattern[j]:
                j += 1
            if j == len_p:
                res += 1
                j = lps[j-1]
        return res