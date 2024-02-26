# 0329 - Longest Increasing Path in a Matrix
# Date: 2023-10-10
# Runtime: 396 ms, Memory: 17.3 MB
# Submission Id: 1071782073


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])        
        in_degree = [[0] * len_c for _ in range(len_r)]
        
        for r in range(len_r):
            for c in range(len_c):
                for next_r, next_c in (r+1, c), (r, c+1), (r-1, c), (r, c-1):
                    if (0 <= next_r < len_r and 0 <= next_c < len_c
                        and matrix[r][c] < matrix[next_r][next_c]):
                        in_degree[next_r][next_c] += 1
        print(in_degree)                
        queue = deque([(r, c) for r in range(len_r) for c in range(len_c) if in_degree[r][c] == 0])
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for next_r, next_c in (r+1, c), (r, c+1), (r-1, c), (r, c-1):
                    if (0 <= next_r < len_r and 0 <= next_c < len_c
                       and matrix[r][c] < matrix[next_r][next_c]):
                        in_degree[next_r][next_c] -= 1
                        if in_degree[next_r][next_c] == 0:
                            queue.append((next_r, next_c))
            step += 1
        return step