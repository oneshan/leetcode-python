# 1391 - Counting Elements
# Date: 2022-10-14
# Runtime: 74 ms, Memory: 14 MB
# Submission Id: 822288333


from collections import defaultdict
class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums_set = set(arr)

        ans = 0
        for num in arr:
            ans += (num+1 in nums_set)
        return ans