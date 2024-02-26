# 1753 - Path With Minimum Effort
# Date: 2022-10-13
# Runtime: 7125 ms, Memory: 16 MB
# Submission Id: 821580300


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        len_r, len_c = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        
        def check(effort):
            seen = {(0,0)}
            stack = [(0, 0)]
            while stack:
                row, col = stack.pop()
                if row == len_r-1 and col == len_c-1:
                    return True
                for dx, dy in directions:
                    new_x, new_y = row+dx, col+dy
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