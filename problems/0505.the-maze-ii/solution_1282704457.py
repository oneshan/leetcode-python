# 0505 - The Maze II
# Date: 2024-06-09
# Runtime: 215 ms, Memory: 17.2 MB
# Submission Id: 1282704457


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        len_r, len_c = len(maze), len(maze[0])

        ans = float('inf')
        heap = [(0, start[0], start[1])]
        seen = {(start[0], start[1]): 0}

        while heap:
            step, r, c = heapq.heappop(heap)
            if r == destination[0] and c == destination[1]:
                return step

            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                new_r, new_c, new_step = r, c, step
                while 0 <= new_r + dr < len_r and 0 <= new_c + dc < len_c and maze[new_r+dr][new_c+dc] == 0:
                    new_step += 1
                    new_r += dr
                    new_c += dc

                if (new_r, new_c) not in seen or seen[(new_r, new_c)] > new_step:
                    seen[(new_r, new_c)] = new_step
                    heapq.heappush(heap, (new_step, new_r, new_c))
        
        return -1