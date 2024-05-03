# 2524 - Largest Positive Integer That Exists With Its Negative
# Date: 2024-05-02
# Runtime: 107 ms, Memory: 16.8 MB
# Submission Id: 1247048703


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nset = set()
        ans = -1
        for num in nums:
            abs_num = abs(num)
            if abs_num > ans and -num + 1024 in nset:
                ans = abs_num
            nset.add(num + 1024)
        return ans