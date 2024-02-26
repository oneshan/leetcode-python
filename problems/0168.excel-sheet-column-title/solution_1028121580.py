# 0168 - Excel Sheet Column Title
# Date: 2023-08-22
# Runtime: 37 ms, Memory: 16.1 MB
# Submission Id: 1028121580


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber:
            columnNumber -= 1
            columnNumber, r = divmod(columnNumber, 26)
            title.append(chr(ord('A')+r))
        return ''.join(title[::-1])