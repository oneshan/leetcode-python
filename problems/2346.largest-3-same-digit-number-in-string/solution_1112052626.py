# 2346 - Largest 3-Same-Digit Number in String
# Date: 2023-12-04
# Runtime: 44 ms, Memory: 16.3 MB
# Submission Id: 1112052626


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ""
        n = len(num)
        for i in range(2, n):
            if num[i-2] == num[i-1] == num[i]:
                ans = max(ans, num[i])
        return ans * 3