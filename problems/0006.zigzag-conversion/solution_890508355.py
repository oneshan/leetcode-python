# 0006 - Zigzag Conversion
# Date: 2023-02-03
# Runtime: 88 ms, Memory: 14 MB
# Submission Id: 890508355


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        pos = 0
        direct = -1
        for ch in s:
            if pos in (0, numRows - 1):
                direct *= -1
            rows[pos].append(ch)
            pos += 1 * direct
        
        return ''.join(''.join(ch for ch in row) for row in rows)