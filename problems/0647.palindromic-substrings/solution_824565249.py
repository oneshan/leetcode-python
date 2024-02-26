# 0647 - Palindromic Substrings
# Date: 2022-10-18
# Runtime: 369 ms, Memory: 13.9 MB
# Submission Id: 824565249


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def recur(left, right):
            count = 0
            while 0 <= left and right < len(s):
                if s[left] != s[right]:
                    break 
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(len(s)):
            ans += recur(i, i) + recur(i, i+1)
        return ans
            