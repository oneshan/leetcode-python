# 0151 - Reverse Words in a String
# Date: 2024-02-17
# Runtime: 34 ms, Memory: 16.7 MB
# Submission Id: 1177725069


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])