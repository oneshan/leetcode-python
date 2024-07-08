# 0459 - Repeated Substring Pattern
# Date: 2024-05-16
# Runtime: 73 ms, Memory: 17.1 MB
# Submission Id: 1259576167


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        def get_lsp(pattern):
            lsp = [0] * len(pattern)

            j = 0
            for i in range(1, len(pattern)):
                while j and pattern[i] != pattern[j]:
                    j = lsp[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lsp[i] = j

            return lsp

        lsp = get_lsp(s)
        return lsp[-1] and len(s) % (len(s) - lsp[-1]) == 0