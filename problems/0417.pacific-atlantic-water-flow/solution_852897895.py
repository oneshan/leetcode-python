# 0417 - Pacific Atlantic Water Flow
# Date: 2022-12-01
# Runtime: 678 ms, Memory: 15.5 MB
# Submission Id: 852897895


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(heights), len(heights[0])
        
        def dfs(stack):
            seen = set()
            while stack:
                r, c = stack.pop()
                if (r, c) in seen:
                    continue
                seen.add((r, c))
                if 0 < r and heights[r][c] <= heights[r-1][c]: stack.append((r-1, c))
                if 0 < c and heights[r][c] <= heights[r][c-1]: stack.append((r, c-1))
                if r < len_r-1 and heights[r][c] <= heights[r+1][c]: stack.append((r+1, c))
                if c < len_c-1 and heights[r][c] <= heights[r][c+1]: stack.append((r, c+1))
            return seen
        
        
        stack_p = []
        stack_a = []
        for r in range(len_r):
            stack_p.append([r, 0])
            stack_a.append([r, len_c-1])
        for c in range(len_c):
            stack_p.append([0, c])
            stack_a.append([len_r-1, c])
            
        return dfs(stack_p) & dfs(stack_a)