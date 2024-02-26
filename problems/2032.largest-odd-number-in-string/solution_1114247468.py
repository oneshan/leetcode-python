# 2032 - Largest Odd Number in String
# Date: 2023-12-07
# Runtime: 50 ms, Memory: 17.9 MB
# Submission Id: 1114247468


class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)        
        for i in range(n-1, -1, -1):
            if int(num[i]) & 1:
                return num[:i+1]
        return ""