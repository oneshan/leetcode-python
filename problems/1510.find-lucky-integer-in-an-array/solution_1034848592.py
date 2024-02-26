# 1510 - Find Lucky Integer in an Array
# Date: 2023-08-29
# Runtime: 62 ms, Memory: 16.5 MB
# Submission Id: 1034848592


from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = -1
        for val, count in counter.items():
            if val == count:
                ans = max(ans, val)
        return ans