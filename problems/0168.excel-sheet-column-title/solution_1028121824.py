# 0168 - Excel Sheet Column Title
# Date: 2023-08-22
# Runtime: 40 ms, Memory: 16.3 MB
# Submission Id: 1028121824


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber:
            columnNumber, r = divmod(columnNumber-1, 26)
            title.append(chr(ord('A')+r))
        return ''.join(title[::-1])