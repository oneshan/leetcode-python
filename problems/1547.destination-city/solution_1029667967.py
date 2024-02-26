# 1547 - Destination City
# Date: 2023-08-23
# Runtime: 56 ms, Memory: 16.5 MB
# Submission Id: 1029667967


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_cities, to_cities = set(), set()
        for _from, _to in paths:
            from_cities.add(_from)
            to_cities.add(_to)
            
        return list(to_cities - from_cities)[0]