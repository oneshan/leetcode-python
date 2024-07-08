# 0647 - Palindromic Substrings
# Date: 2024-05-27
# Runtime: 132 ms, Memory: 16.4 MB
# Submission Id: 1268968649


class Solution:
    def countSubstrings(self, s: str) -> int:
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
            ans += recur(i, i)
            ans += recur(i, i+1)
        return ans