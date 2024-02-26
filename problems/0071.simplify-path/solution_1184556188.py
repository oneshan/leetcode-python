# 0071 - Simplify Path
# Date: 2024-02-24
# Runtime: 36 ms, Memory: 16.7 MB
# Submission Id: 1184556188


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '.' or not part:
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)