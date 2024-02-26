# 1547 - Destination City
# Date: 2023-08-29
# Runtime: 60 ms, Memory: 16.4 MB
# Submission Id: 1034845282


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        table = {}
        for _from, _to in paths:
            table[_from] = _to
        
        start = paths[0][0]
        while start in table:
            start = table[start]
        return start