# 2038 - Nearest Exit from Entrance in Maze
# Date: 2022-11-21
# Runtime: 2102 ms, Memory: 14.4 MB
# Submission Id: 847465586


from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        len_r, len_c = len(maze), len(maze[0])
        
        step = 0
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            row, col, step = queue.popleft()
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                next_r, next_c = row+dr, col+dc
                if 0 <= next_r < len_r and 0 <= next_c < len_c and maze[next_r][next_c] == '.':
                    if next_r in (0, len_r-1) or next_c in (0, len_c-1):
                        return step+1
                    queue.append((next_r, next_c, step+1))
                    maze[next_r][next_c] = '+'
        return -1