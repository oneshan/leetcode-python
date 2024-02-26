# 0647 - Palindromic Substrings
# Date: 2024-02-10
# Runtime: 62 ms, Memory: 16.5 MB
# Submission Id: 1171061262


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        def recur(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        ans = 0
        for i in range(n):
            ans += recur(i, i) + recur(i, i+1)
        return ans
