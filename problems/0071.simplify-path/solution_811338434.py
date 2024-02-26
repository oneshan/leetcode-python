# 0071 - Simplify Path
# Date: 2022-09-29
# Runtime: 85 ms, Memory: 14.1 MB
# Submission Id: 811338434


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        folder_name = ''
        for ch in path:
            if ch != '/':
                folder_name += ch
                continue
            if not folder_name:
                continue
            if folder_name == '..':
                if stack: stack.pop()
            elif folder_name != '.':
                stack.append(folder_name)
            folder_name = ''
        print(stack, folder_name)
        
        if folder_name:
            if folder_name == '..':
                if stack: stack.pop()
            elif folder_name != '.':
                stack.append(folder_name)
                            
        return '/' + '/'.join(stack)