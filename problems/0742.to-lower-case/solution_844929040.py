# 0742 - To Lower Case
# Date: 2022-11-17
# Runtime: 27 ms, Memory: 13.8 MB
# Submission Id: 844929040


class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([chr(ord(ch) | 32) if 'A' <= ch <= 'Z' else ch for ch in s])