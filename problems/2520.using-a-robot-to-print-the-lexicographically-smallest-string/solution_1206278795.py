# 2520 - Using a Robot to Print the Lexicographically Smallest String
# Date: 2024-03-17
# Runtime: 368 ms, Memory: 19.2 MB
# Submission Id: 1206278795


class Solution:
    def robotWithString(self, s: str) -> str:
        queue = deque()
        stack = []
        ans = []

        for ch in s:
            while queue and queue[-1] > ch:
                queue.pop()
            queue.append(ch)

        for ch in s:
            stack.append(ch)
            if queue and queue[0] == ch:
                queue.popleft()
                while stack and queue and stack[-1] <= queue[0]:
                    ans.append(stack.pop())
        
        while stack:
            ans.append(stack.pop())
        return ''.join(ans)