# 1293 - Three Consecutive Odds
# Date: 2024-07-01
# Runtime: 43 ms, Memory: 16.6 MB
# Submission Id: 1305500450


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] & 1:
                count += 1
            if i >= 3:
                count -= (arr[i-3] & 1)
            if count == 3:
                return True
        return False