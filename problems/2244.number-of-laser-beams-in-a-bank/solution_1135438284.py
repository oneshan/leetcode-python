# 2244 - Number of Laser Beams in a Bank
# Date: 2024-01-03
# Runtime: 258 ms, Memory: 19.4 MB
# Submission Id: 1135438284


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0
        for row in bank:
            curr = sum(ch == '1' for ch in row)
            if curr:
                ans += prev * curr
                prev = curr
        return ans