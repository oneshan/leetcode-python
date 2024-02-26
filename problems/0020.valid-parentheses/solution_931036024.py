# 0020 - Valid Parentheses
# Date: 2023-04-10
# Runtime: 31 ms, Memory: 13.8 MB
# Submission Id: 931036024


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        stack = []
        for ch in s:
            if ch in mapping:
                if not stack:
                    return False
                prev = stack.pop()
                if prev != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0