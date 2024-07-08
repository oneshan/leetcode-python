# 0417 - Pacific Atlantic Water Flow
# Date: 2024-05-20
# Runtime: 195 ms, Memory: 18.1 MB
# Submission Id: 1262870287


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(heights), len(heights[0])
        
        pacifics = []
        atlantics = []
        for r in range(len_r):
            pacifics.append((r, 0))
            atlantics.append((r, len_c-1))
        for c in range(len_c):
            pacifics.append((0, c))
            atlantics.append((len_r-1, c))
        
        def bfs(borders):
            queue = deque(borders)
            seen = set(borders)
            while queue:
                r, c = queue.popleft()
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        seen.add((nr, nc))            
                        queue.append((nr, nc))
            return seen

        return bfs(pacifics) & bfs(atlantics)