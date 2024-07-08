# 0329 - Longest Increasing Path in a Matrix
# Date: 2024-05-27
# Runtime: 342 ms, Memory: 21.3 MB
# Submission Id: 1269021969


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        len_r, len_c = len(matrix), len(matrix[0])
        graph = defaultdict(list)
        indegree = [[0] * len_c for _ in range(len_r)]

        for r in range(len_r):
            for c in range(len_c):
                for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                    if 0 <= nr < len_r and 0 <= nc < len_c and matrix[r][c] < matrix[nr][nc]:
                        graph[(r, c)].append((nr, nc))
                        indegree[nr][nc] += 1

        queue = deque([(r, c) for r in range(len_r) for c in range(len_c) if indegree[r][c] == 0])
        ans = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in graph[(r, c)]:
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        queue.append((nr, nc))
            ans += 1
        return ans