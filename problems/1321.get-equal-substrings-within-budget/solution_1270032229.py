# 1321 - Get Equal Substrings Within Budget
# Date: 2024-05-28
# Runtime: 63 ms, Memory: 18.1 MB
# Submission Id: 1270032229


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(ss) - ord(tt)) for ss, tt in zip(s, t)]
        n = len(s)

        ans = 0
        left = curr = 0
        for right in range(n):
            curr += cost[right]
            while curr > maxCost:
                curr -= cost[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans