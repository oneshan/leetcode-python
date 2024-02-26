# 1391 - Counting Elements
# Date: 2022-10-14
# Runtime: 43 ms, Memory: 14.1 MB
# Submission Id: 822288442


class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums_set = set(arr)

        ans = 0
        for num in arr:
            ans += (num+1 in nums_set)
        return ans