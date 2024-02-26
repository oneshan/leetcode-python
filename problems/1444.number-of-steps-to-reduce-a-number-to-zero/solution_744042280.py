# 1444 - Number of Steps to Reduce a Number to Zero
# Date: 2022-07-11
# Runtime: 48 ms, Memory: 13.9 MB
# Submission Id: 744042280


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            count += 1
        return count