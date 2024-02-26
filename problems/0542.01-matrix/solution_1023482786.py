# 0542 - 01 Matrix
# Date: 2023-08-17
# Runtime: 550 ms, Memory: 19.5 MB
# Submission Id: 1023482786


from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(mat), len(mat[0])
        
        ans = [[-1] * len_c for _ in range(len_r)]
        
        queue = deque()
        for r in range(len_r):
            for c in range(len_c):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if ans[r][c] != -1:
                    continue
                ans[r][c] = step
                for dr, dc in (0, -1), (0, 1), (1, 0), (-1, 0):
                    next_r, next_c = r+dr, c+dc
                    if 0 <= next_r < len_r and 0 <= next_c < len_c and ans[next_r][next_c] == -1:
                        queue.append((next_r, next_c))
            step += 1
        return ans