# 2597 - Cycle Length Queries in a Tree
# Date: 2022-12-18
# Runtime: 4837 ms, Memory: 53.7 MB
# Submission Id: 861454187


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def calculate(a, b):
            count = 0
            while a and b:
                count += 1
                if a > b:
                    a >>= 1
                elif a < b:
                    b >>= 1
                else:
                    break
            return count
        
        return [calculate(a, b) for a, b in queries]