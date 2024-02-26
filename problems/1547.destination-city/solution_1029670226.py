# 1547 - Destination City
# Date: 2023-08-23
# Runtime: 70 ms, Memory: 16.3 MB
# Submission Id: 1029670226


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = dict(paths)
        ans = None
        
        city = paths[0][0]
        while city in graph:
            city = graph[city]
        return city