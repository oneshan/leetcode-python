# 3181 - Find Building Where Alice and Bob Can Meet
# Date: 2023-11-20
# Runtime: 1630 ms, Memory: 40.1 MB
# Submission Id: 1102174947


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        
        next_greater = {}
        stack = []
        for idx in range(n):
            while stack and heights[stack[-1]] < heights[idx]:
                prev_idx = stack.pop()
                next_greater[prev_idx] = idx
            stack.append(idx)
                    
        def get_ans(a, b):
            if a == b:
                return a
            if a > b:
                return get_ans(b, a)
            if heights[a] < heights[b]:
                return b
            
            if next_greater.get(a, n) > b:
                return next_greater[a] if a in next_greater else -1

            next_idx = next_greater.get(b, n)
            while next_idx < n:
                if heights[next_idx] > heights[a]:
                    return next_idx
                next_idx = next_greater.get(next_idx, n)
            return -1
        
        return [get_ans(a, b) for a, b in queries]