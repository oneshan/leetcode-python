# 2038 - Nearest Exit from Entrance in Maze
# Date: 2023-09-16
# Runtime: 747 ms, Memory: 16.9 MB
# Submission Id: 1050819949


from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        len_r, len_c = len(maze), len(maze[0])
        
        def valid(r, c):
            return 0 <= r < len_r and 0 <= c < len_c and maze[r][c] == '.'
        
        queue = deque([entrance])
        maze[entrance[0]][entrance[1]] = '+'
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if not valid(dr, dc):
                        continue
                    if dr in (0, len_r-1) or dc in (0, len_c-1):
                        return step + 1
                    maze[dr][dc] = '+'
                    queue.append((dr, dc))
            step += 1
        return -1