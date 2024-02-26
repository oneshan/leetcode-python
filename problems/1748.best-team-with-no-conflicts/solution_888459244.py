# 1748 - Best Team With No Conflicts
# Date: 2023-01-31
# Runtime: 2102 ms, Memory: 14.2 MB
# Submission Id: 888459244


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(ages, scores))
        dp = [score for _, score in arr]
        n = len(arr)
        
        for i in range(n):
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    dp[i] = max(dp[i], dp[j] + arr[i][1])
        return max(dp)