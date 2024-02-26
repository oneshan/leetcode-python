# 1797 - Goal Parser Interpretation
# Date: 2022-11-16
# Runtime: 64 ms, Memory: 13.8 MB
# Submission Id: 844324007


class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        
        is_open = False
        for ch in command:
            if ch == ')':
                if is_open:
                    ans.append('o')
                is_open = False
            elif ch == '(':
                is_open = True
            else:
                is_open = False
                ans.append(ch)
        
        return ''.join(ans)