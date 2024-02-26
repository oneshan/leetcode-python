# 0542 - 01 Matrix
# Date: 2022-12-31
# Runtime: 726 ms, Memory: 17.3 MB
# Submission Id: 868434242


from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(mat), len(mat[0])
        
        ans = [[float('inf')] * len_c for _ in range(len_r)]
        queue = deque()
        for r in range(len_r):
            for c in range(len_c):
                if mat[r][c] == 0:
                    ans[r][c] = 0
                    queue.append((r, c))
            
        distance = 0
        while queue:
            r, c = queue.popleft()
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                new_r, new_c = r+dx, c+dy
                if 0 <= new_r < len_r and 0 <= new_c < len_c:
                    if ans[new_r][new_c] == float('inf'):
                        ans[new_r][new_c] = ans[r][c] + 1
                        queue.append((new_r, new_c))
            
        return ans