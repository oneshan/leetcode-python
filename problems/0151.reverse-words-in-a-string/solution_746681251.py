# 0151 - Reverse Words in a String
# Date: 2022-07-14
# Runtime: 51 ms, Memory: 13.8 MB
# Submission Id: 746681251


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])