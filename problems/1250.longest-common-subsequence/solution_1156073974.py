# 1250 - Longest Common Subsequence
# Date: 2024-01-25
# Runtime: 372 ms, Memory: 16.5 MB
# Submission Id: 1156073974


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1, len_2 = len(text1), len(text2)
        
        prev = [0] * (len_2 + 1)
        curr = [0] * (len_2 + 1)

        for row in range(len_1):
            for col in range(len_2):
                if text1[row] == text2[col]:
                    curr[col+1] = prev[col] + 1
                else:
                    curr[col+1] = max(curr[col], prev[col+1])
            prev, curr = curr, prev
        return prev[-1]