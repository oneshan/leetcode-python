# 0394 - Decode String
# Date: 2022-07-24
# Runtime: 53 ms, Memory: 13.9 MB
# Submission Id: 755345419


class Solution:
    def decodeString(self, s: str) -> str:
        num = ""
        stack = [""]
        
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
                stack.append("")
            else:
                stack[-1] = ch + stack[-1]
        
        if num:
            tmp = int(num) * stack.pop()
            stack[-1] = tmp + stack[-1]
        return stack[0]