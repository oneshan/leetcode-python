# 0542 - 01 Matrix
# Date: 2023-09-16
# Runtime: 561 ms, Memory: 19.8 MB
# Submission Id: 1050669074


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
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for next_r, next_c in (r+1, c), (r, c+1), (r-1, c), (r, c-1):
                    if 0 <= next_r < len_r and 0 <= next_c < len_c:
                        if ans[next_r][next_c] == float('inf'):
                            ans[next_r][next_c] = ans[r][c] + 1
                            queue.append((next_r, next_c))
        return ans