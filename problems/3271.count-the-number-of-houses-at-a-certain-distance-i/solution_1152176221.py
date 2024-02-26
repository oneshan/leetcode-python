# 3271 - Count the Number of Houses at a Certain Distance I
# Date: 2024-01-21
# Runtime: 185 ms, Memory: 16.7 MB
# Submission Id: 1152176221


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0] * n
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                dist = min(abs(j-i),
                           abs(i-x) + 1 + abs(j-y),
                           abs(i-y) + 1 + abs(j-x),
                          )
                ans[dist-1] += 2
        return ans
