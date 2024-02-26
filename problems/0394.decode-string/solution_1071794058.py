# 0394 - Decode String
# Date: 2023-10-10
# Runtime: 36 ms, Memory: 16.3 MB
# Submission Id: 1071794058


class Solution:
    def decodeString(self, s: str) -> str:
        num, stack = "", [""]
        
        for ch in reversed(s):
            if ch.isdigit():
                num = ch + num
                continue
                
            if num:
                tmp = int(num) * stack.pop()
                stack[-1] = tmp + stack[-1]
                num = ""
            
            if ch == '[':
                continue
            elif ch == ']':
                stack.append('')
            else:
                stack[-1] = ch + stack[-1]
        
        if num:
            stack[0] = int(num) * stack.pop() + stack[0]
            
        return stack[0]
    