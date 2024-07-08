# 0388 - Longest Absolute File Path
# Date: 2024-06-20
# Runtime: 38 ms, Memory: 16.5 MB
# Submission Id: 1294345377


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
            stack.append((1+length, depth))
            if '.' in name:
                res = max(res, length)
        return res