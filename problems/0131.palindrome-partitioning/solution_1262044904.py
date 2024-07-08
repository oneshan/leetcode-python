# 0131 - Palindrome Partitioning
# Date: 2024-05-19
# Runtime: 445 ms, Memory: 35.2 MB
# Submission Id: 1262044904


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []

        dp = [[False] * n for _ in range(n)]

        def backtrack(arr, i):
            if i == n:
                ans.append(arr[:])
                return
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    arr.append(s[i:j+1])
                    backtrack(arr, j+1)
                    arr.pop()

        backtrack([], 0)
        return ans