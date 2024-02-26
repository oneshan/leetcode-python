# 2337 - Remove Digit From Number to Maximize Result
# Date: 2022-10-13
# Runtime: 55 ms, Memory: 13.9 MB
# Submission Id: 821643775


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = ""
        for idx in range(len(number)):
            if number[idx] == digit:
                candidate = number[:idx] + number[idx+1:]
                if ans < candidate:
                    ans = candidate
        return ans