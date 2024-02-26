# 0316 - Remove Duplicate Letters
# Date: 2023-09-26
# Runtime: 41 ms, Memory: 16.1 MB
# Submission Id: 1059721053


from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        
        last_pos = defaultdict(int)
        for idx, ch in enumerate(s):
            last_pos[ch] = idx
            
        for idx, ch in enumerate(s):
            if ch in seen:
                continue
            while stack and stack[-1] > ch and last_pos[stack[-1]] > idx:
                seen.discard(stack[-1])
                stack.pop()
            seen.add(ch)
            stack.append(ch)
            
        return ''.join(stack)