# 0071 - Simplify Path
# Date: 2024-02-24
# Runtime: 28 ms, Memory: 16.5 MB
# Submission Id: 1184557294


class Solution:
    def simplifyPath(self, path: str) -> str:

        def split(string, trim):
            chunk = []
            for ch in string:
                if ch == trim:
                    yield ''.join(chunk)
                    chunk = []
                else:
                    chunk.append(ch)
            yield ''.join(chunk)

        stack = []
        for part in split(path, '/'):
            if part == '.' or not part:
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)