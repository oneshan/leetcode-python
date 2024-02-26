# 1510 - Find Lucky Integer in an Array
# Date: 2023-10-25
# Runtime: 64 ms, Memory: 16.3 MB
# Submission Id: 1083689280


from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = -1
        for num, count in counter.items():
            if num == count:
                ans = max(ans, num)
        return ans