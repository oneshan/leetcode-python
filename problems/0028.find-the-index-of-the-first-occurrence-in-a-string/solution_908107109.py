# 0028 - Find the Index of the First Occurrence in a String
# Date: 2023-03-03
# Runtime: 36 ms, Memory: 13.9 MB
# Submission Id: 908107109


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h, len_n = len(haystack), len(needle)
        if len_h < len_n:
            return -1
        
        for i in range(len_h-len_n+1):
            for j in range(len_n):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1