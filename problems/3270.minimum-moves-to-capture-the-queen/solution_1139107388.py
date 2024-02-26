# 3270 - Minimum Moves to Capture The Queen
# Date: 2024-01-07
# Runtime: 26 ms, Memory: 17.4 MB
# Submission Id: 1139107388


class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # (a, b) denotes the position of the white rook.
        # (c, d) denotes the position of the white bishop.
        # (e, f) denotes the position of the black queen.
        if a == e:
            if c == a and (b > d > f or b < d < f):
                return 2
            return 1
        
        if b == f:
            if d == b and (a > c > e or a < c < e):
                return 2
            return 1
        
        if abs(c-e) == abs(d-f):
            if (c < a < e or c > a > e) and (d > b > f or d < b < f):
                if abs(a-c) == abs(b-d):
                    return 2
            return 1
        
        return 2