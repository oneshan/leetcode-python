# 2346 - Largest 3-Same-Digit Number in String
# Date: 2023-12-04
# Runtime: 39 ms, Memory: 16.2 MB
# Submission Id: 1112051855


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ""
        prev, count = "", 0
        for ch in num:
            if prev == ch:
                count += 1
                if count == 3:
                    ans = max(ans, ch)
            else:
                prev, count = ch, 1
        return ans * 3