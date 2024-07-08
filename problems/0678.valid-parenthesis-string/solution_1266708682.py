# 0678 - Valid Parenthesis String
# Date: 2024-05-24
# Runtime: 39 ms, Memory: 16.6 MB
# Submission Id: 1266708682


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        left = right = 0
        for i in range(n):
            if s[i] == '(' or s[i] == '*':
                left += 1
            else:
                right += 1
            
            if left < right:
                return False

        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left > right:
                return False
        
        return True