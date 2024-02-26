# 0071 - Simplify Path
# Date: 2023-09-04
# Runtime: 34 ms, Memory: 16.4 MB
# Submission Id: 1040006158


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for part in path.split('/'):
            if part == '.' or not part:
                continue
            if part == '..':
                if stack: stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)