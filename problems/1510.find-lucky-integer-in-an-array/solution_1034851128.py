# 1510 - Find Lucky Integer in an Array
# Date: 2023-08-29
# Runtime: 66 ms, Memory: 16.4 MB
# Submission Id: 1034851128


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        ans, count, prev = -1, 0, None
        for num in arr:
            if num != prev:
                if prev == count:
                    ans = prev
                prev, count = num, 0
            count += 1
        if prev == count:
            ans = prev
        return ans