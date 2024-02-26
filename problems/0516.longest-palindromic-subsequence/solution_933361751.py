# 0516 - Longest Palindromic Subsequence
# Date: 2023-04-14
# Runtime: 1092 ms, Memory: 237.2 MB
# Submission Id: 933361751


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @cache
        def recur(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                return recur(left+1, right-1) + 2
            return max(recur(left, right-1), recur(left+1, right))
        
        return recur(0, n-1)