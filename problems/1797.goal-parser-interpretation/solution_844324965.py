# 1797 - Goal Parser Interpretation
# Date: 2022-11-16
# Runtime: 64 ms, Memory: 13.9 MB
# Submission Id: 844324965


class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        
        prev = None
        for ch in command:
            if ch not in '()':
                ans.append(ch)
            if ch == ')' and prev =='(':
                ans.append('o')
            prev = ch
        
        return ''.join(ans)