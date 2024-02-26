# 0879 - Maximize Distance to Closest Person
# Date: 2023-10-10
# Runtime: 115 ms, Memory: 17.1 MB
# Submission Id: 1071749339


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        
        ans, left = 0, -1
        for right in range(n):
            if seats[right] == 1:
                if left == -1:
                    ans = max(ans, right)
                else:
                    ans = max(ans, (right - left) // 2)
                left = right
        if seats[-1] == 0:
            ans = max(ans, right - left)
        return ans