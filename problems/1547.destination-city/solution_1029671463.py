# 1547 - Destination City
# Date: 2023-08-23
# Runtime: 60 ms, Memory: 16.4 MB
# Submission Id: 1029671463


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_cities, to_cities = set(), set()
        for _from, _to in paths:
            from_cities.add(_from)
            to_cities.add(_to)
            
        return max(to_cities - from_cities)