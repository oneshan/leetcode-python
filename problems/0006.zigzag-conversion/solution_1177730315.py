# 0006 - Zigzag Conversion
# Date: 2024-02-17
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1177730315


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        arr = [[] for _ in range(numRows)]
        i, dx = 0, 1
        for ch in s:
            arr[i].append(ch)
            i += dx
            if i == numRows-1:
                dx = -1
            if i == 0:
                dx = 1
        return ''.join([''.join(string) for string in arr])