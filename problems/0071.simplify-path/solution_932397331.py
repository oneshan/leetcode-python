# 0071 - Simplify Path
# Date: 2023-04-12
# Runtime: 31 ms, Memory: 13.9 MB
# Submission Id: 932397331


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for part in path.split('/'):
            if part == '..':
                if stack: stack.pop()
            elif part == '.' or not part:
                continue
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)