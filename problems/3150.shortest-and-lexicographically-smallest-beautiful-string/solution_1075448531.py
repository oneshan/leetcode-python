# 3150 - Shortest and Lexicographically Smallest Beautiful String
# Date: 2023-10-15
# Runtime: 50 ms, Memory: 16.4 MB
# Submission Id: 1075448531


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        
        count = 0
        ans = ""
        for right in range(n):
            if s[right] == '1':
                count += 1
            while count > k:
                if s[left] == '1':
                    count -= 1
                left += 1
            while left < right and s[left] == '0':
                left += 1
            if count == k:
                candidate = s[left:right+1]
                if not ans or int(ans) > int(candidate):
                    ans = candidate
        return ans