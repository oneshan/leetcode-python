# 2163 - Kth Distinct String in an Array
# Date: 2022-05-08
# Runtime: 94 ms, Memory: 14.3 MB
# Submission Id: 695423418


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for string in arr:
            seen[string] = seen.get(string, 0) + 1
            
        for string in arr:
            if seen[string] == 1:
                k -= 1
            if k == 0:
                return string
        return ""