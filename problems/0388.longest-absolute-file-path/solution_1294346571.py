# 0388 - Longest Absolute File Path
# Date: 2024-06-20
# Runtime: 33 ms, Memory: 16.8 MB
# Submission Id: 1294346571


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [[0, -1]]
        res = 0

        for line in input.split('\n'):
            temp = line.split('\t')
            depth, name = len(temp)-1, temp[-1]

            while stack[-1][1] >= depth:
                stack.pop()
            
            length = len(name) + stack[-1][0]
            if '.' in name:
                res = max(res, length)
            else:
                stack.append((1+length, depth))

        return res