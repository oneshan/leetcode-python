# 2597 - Cycle Length Queries in a Tree
# Date: 2022-12-18
# Runtime: 2347 ms, Memory: 53.7 MB
# Submission Id: 861403125


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def calculate(a, b):
            count = 1
            while a and b:
                if a > b:
                    a >>= 1
                    count += 1
                elif a < b:
                    b >>= 1
                    count += 1
                else:
                    break
            return count
        
        return [calculate(a, b) for a, b in queries]