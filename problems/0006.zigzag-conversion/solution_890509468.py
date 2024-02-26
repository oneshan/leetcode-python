# 0006 - Zigzag Conversion
# Date: 2023-02-03
# Runtime: 82 ms, Memory: 14.1 MB
# Submission Id: 890509468


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        numRows -= 1
        
        for idx, ch in enumerate(s):
            rows[abs((idx+numRows) % (2*numRows) - numRows)].append(ch)
                
        return ''.join(''.join(ch for ch in row) for row in rows)