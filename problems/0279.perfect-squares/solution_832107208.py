# 0279 - Perfect Squares
# Date: 2022-10-28
# Runtime: 834 ms, Memory: 14.9 MB
# Submission Id: 832107208


from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        perfect = [i*i for i in range(1, int(n**0.5)+1)]
        if n in perfect:
            return 1
        
        queue = deque([n])
        level = 0
        seen = set()
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                num = queue.popleft()
                for square in perfect:
                    next_num = num - square
                    if next_num == 0:
                        return level
                    if next_num < 0:
                        break
                    if next_num not in seen:
                        queue.append(next_num)
                        seen.add(next_num)
        return -1