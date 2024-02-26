# 0006 - Zigzag Conversion
# Date: 2023-02-03
# Runtime: 68 ms, Memory: 13.9 MB
# Submission Id: 890506775


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        pos = 0
        direct = -1
        for ch in s:
            if pos in (0, numRows - 1):
                direct *= -1
            rows[pos] += ch
            pos += 1 * direct
        return ''.join(row for row in rows)