# 0028 - Find the Index of the First Occurrence in a String
# Date: 2023-03-03
# Runtime: 33 ms, Memory: 13.9 MB
# Submission Id: 908110712


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h, len_n = len(haystack), len(needle)
        if len_h < len_n:
            return -1
        
        # compute prefix
        prefix = [0] * len_n
        j = 0
        for i in range(1, len_n):
            while j and needle[i] != needle[j]:
                j = prefix[j-1]
            if needle[i] == needle[j]:
                prefix[i] = j+1
                j += 1

        # find pattern
        j = 0
        for i in range(len_h):
            while j and haystack[i] != needle[j]:
                j = prefix[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len_n:
                return i-j+1
        return -1