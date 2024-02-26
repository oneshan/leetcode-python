# 1627 - Last Moment Before All Ants Fall Out of a Plank
# Date: 2023-11-04
# Runtime: 158 ms, Memory: 17.2 MB
# Submission Id: 1091102542


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for num in left:
            ans = max(ans, num)
        for num in right:
            ans = max(ans, n-num)
        return ans