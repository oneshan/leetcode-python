# 0490 - The Maze
# Date: 2024-06-09
# Runtime: 205 ms, Memory: 17.1 MB
# Submission Id: 1282679924


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        len_r, len_c = len(maze), len(maze[0])

        seen = set()
        queue = deque([start])
        seen.add((start[0], start[1]))
        while queue:
            r, c = queue.popleft()
            if r == destination[0] and c == destination[1]:
                return True
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                new_r, new_c = r+dr, c+dc
                while 0 <= new_r < len_r and 0 <= new_c < len_c and maze[new_r][new_c] == 0:
                    new_r += dr
                    new_c += dc
                
                new_r -= dr
                new_c -= dc

                if (new_r, new_c) not in seen:
                    seen.add((new_r, new_c))
                    queue.append((new_r, new_c))

        return False