# 3181 - Find Building Where Alice and Bob Can Meet
# Date: 2023-11-19
# Runtime: 1756 ms, Memory: 40.2 MB
# Submission Id: 1101960672


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
        
        @cache
        def recur(idx, target):
            if idx == n:
                return -1
            if heights[idx] >= target:
                return idx
            return recur(next_greater.get(idx, n), target)
            
        def get_ans(a, b):
            if a == b:
                return a
            if a > b and heights[a] > heights[b]:
                return a
            if a < b and heights[a] < heights[b]:
                return b
            init_idx = max(next_greater.get(a, n), next_greater.get(b, n))
            target = max(heights[a], heights[b]) + 1
            return recur(init_idx, target)
        
        return [get_ans(a, b) for a, b in queries]