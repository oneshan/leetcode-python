# 0071 - Simplify Path
# Date: 2023-09-04
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1040005505


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for folder in path.split('/'):
            if folder == '.' or not folder:
                continue
            if folder == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        
        return '/' + '/'.join(stack)