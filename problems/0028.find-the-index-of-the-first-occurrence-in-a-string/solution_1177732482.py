# 0028 - Find the Index of the First Occurrence in a String
# Date: 2024-02-17
# Runtime: 39 ms, Memory: 16.7 MB
# Submission Id: 1177732482


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        lsp = [0] * n
        j = 0
        for i in range(1, n):
            while j and needle[i] != needle[j]:
                j = lsp[j-1]
            if needle[i] == needle[j]:
                j += 1
                lsp[i] = j
        
        j = 0
        for i in range(m):
            while j and haystack[i] != needle[j]:
                j = lsp[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - j + 1
        return -1