# 3181 - Find Building Where Alice and Bob Can Meet
# Date: 2023-11-19
# Runtime: 1903 ms, Memory: 101 MB
# Submission Id: 1101956378


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        
        @cache
        def recur(idx, target):
            if idx == n:
                return -1
            if heights[idx] >= target:
                return idx
            return recur(idx+1, target)
            
        
        def get_ans(a, b):
            if a == b:
                return a
            if a > b and heights[a] > heights[b]:
                return a
            if a < b and heights[a] < heights[b]:
                return b
            init_idx = max(a, b) + 1
            target = max(heights[a], heights[b]) + 1
            return recur(init_idx, target)
        
        return [get_ans(a, b) for a, b in queries]