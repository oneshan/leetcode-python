# 3034 - Points That Intersect With Cars
# Date: 2023-09-10
# Runtime: 82 ms, Memory: 16.3 MB
# Submission Id: 1045184780


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        visited = [False] * 101
        
        for start, end in nums:
            for i in range(start, end+1):
                visited[i] = True
        return sum(visited)