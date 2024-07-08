# 0979 - DI String Match
# Date: 2024-06-07
# Runtime: 51 ms, Memory: 17.7 MB
# Submission Id: 1279698757


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)

        ans = []
        for ch in s:
            if ch == 'I':
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        
        return ans + [left]