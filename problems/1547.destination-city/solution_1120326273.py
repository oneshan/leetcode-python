# 1547 - Destination City
# Date: 2023-12-15
# Runtime: 64 ms, Memory: 16.3 MB
# Submission Id: 1120326273


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_cities, to_cities = set(), set()
        for _from, _to in paths:
            from_cities.add(_from)
            to_cities.add(_to)
            
        return max(to_cities - from_cities)