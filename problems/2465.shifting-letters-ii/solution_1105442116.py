# 2465 - Shifting Letters II
# Date: 2023-11-24
# Runtime: 1159 ms, Memory: 41.8 MB
# Submission Id: 1105442116


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        
        diff = [0] * (n+1)
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            diff[start] += delta
            diff[end+1] -= delta

        ans = []
        curr = 0
        for i in range(n):
            curr += diff[i]
            d = (ord(s[i]) - ord('a') + curr) % 26
            ans.append(chr(ord('a') + d))

        return ''.join(ans)