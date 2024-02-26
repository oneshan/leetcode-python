# 0286 - Walls and Gates
# Date: 2022-10-25
# Runtime: 699 ms, Memory: 17.1 MB
# Submission Id: 829951981


from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        len_r, len_c = len(rooms), len(rooms[0])
        inf = 2147483647
        
        queue = deque()
        for r in range(len_r):
            for c in range(len_c):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                    next_r, next_c = r+dx, c+dy
                    if 0 <= next_r < len_r and 0 <= next_c < len_c:
                        if rooms[next_r][next_c] == 2147483647:
                            queue.append((next_r, next_c))
                            rooms[next_r][next_c] = step