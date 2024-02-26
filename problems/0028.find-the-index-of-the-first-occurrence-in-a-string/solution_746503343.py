# 0028 - Find the Index of the First Occurrence in a String
# Date: 2022-07-14
# Runtime: 63 ms, Memory: 13.9 MB
# Submission Id: 746503343


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1
        
        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1