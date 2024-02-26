# 2101 - Last Day Where You Can Still Cross
# Date: 2023-06-30
# Runtime: 2933 ms, Memory: 25.2 MB
# Submission Id: 983006763


from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def can_cross(row, col, cells, day):
            grid = [[0] * col for _ in range(row)]
            queue = deque()
            
            for r, c in cells[:day]:
                grid[r-1][c-1] = 1
                
            for i in range(col):
                if not grid[0][i]:
                    queue.append((0, i))
                    grid[0][i] = -1
                    
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < row and 0 <= next_c < col and grid[next_r][next_c] == 0:
                        grid[next_r][next_c] = -1
                        queue.append((next_r, next_c))
            return False
        
        left, right = 1, row * col
        while left < right:
            mid = (left + right + 1) // 2
            if can_cross(row, col, cells, mid):
                left = mid
            else:
                right = mid - 1
        return left