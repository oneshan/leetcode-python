# 0499 - The Maze III
# Date: 2024-06-09
# Runtime: 50 ms, Memory: 16.8 MB
# Submission Id: 1282720407


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        len_r, len_c = len(maze), len(maze[0])

        ans = None
        heap = [(0, '', ball[0], ball[1])]
        seen = set()

        while heap:
            step, inst, r, c = heapq.heappop(heap)
            if r == hole[0] and c == hole[1]:
                return inst
            
            if (r, c) in seen:
                continue
            seen.add((r, c))

            for ch, dr, dc in ('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0):
                new_r, new_c, new_step = r, c, step
                while 0 <= new_r + dr < len_r and 0 <= new_c + dc < len_c and maze[new_r+dr][new_c+dc] == 0:
                    new_step += 1
                    new_r += dr
                    new_c += dc
                    if new_r == hole[0] and new_c == hole[1]:
                        break

                heapq.heappush(heap, (new_step, inst + ch, new_r, new_c))
        
        return 'impossible'