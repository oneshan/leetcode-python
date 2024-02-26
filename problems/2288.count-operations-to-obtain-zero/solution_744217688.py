# 2288 - Count Operations to Obtain Zero
# Date: 2022-07-11
# Runtime: 58 ms, Memory: 13.8 MB
# Submission Id: 744217688


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        if num1 < num2:
            num1, num2 = num2, num1
        while num1 and num2:
            count += num1 // num2
            num1, num2 = num2, num1 % num2
        return count