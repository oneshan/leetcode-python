# 0171 - Excel Sheet Column Number
# Date: 2023-08-22
# Runtime: 44 ms, Memory: 16.1 MB
# Submission Id: 1028131642


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord('A') + 1)
        return ans