# 1753 - Path With Minimum Effort
# Date: 2023-09-16
# Runtime: 1954 ms, Memory: 18.4 MB
# Submission Id: 1050895420


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        len_r, len_c = len(heights), len(heights[0])
        
        def check(effort):
            seen = {(0, 0)}
            stack = [(0, 0)]
            while stack:
                row, col = stack.pop()
                if row == len_r-1 and col == len_c-1:
                    return True
                for new_x, new_y in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                    if (0 <= new_x < len_r and 0 <= new_y < len_c
                        and (new_x, new_y) not in seen
                        and abs(heights[new_x][new_y] - heights[row][col]) <= effort
                       ):
                        stack.append((new_x, new_y))
                        seen.add((new_x, new_y))
            return False
        
        left, right = 0, 1000000
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left