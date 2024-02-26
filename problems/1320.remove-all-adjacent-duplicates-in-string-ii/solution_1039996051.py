# 1320 - Remove All Adjacent Duplicates in String II
# Date: 2023-09-04
# Runtime: 86 ms, Memory: 21 MB
# Submission Id: 1039996051


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for ch in s:
            if stack and stack[-1][1] == ch:
                stack[-1][0] += 1
            else:
                stack.append([1, ch])
                
            if stack[-1][0] == k:
                stack.pop()
        
        return ''.join(count * ch for count, ch in stack)