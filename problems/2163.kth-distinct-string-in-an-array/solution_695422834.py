# 2163 - Kth Distinct String in an Array
# Date: 2022-05-08
# Runtime: 117 ms, Memory: 14.1 MB
# Submission Id: 695422834


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        seen_list = []
        for string in arr:
            if string not in seen:
                seen_list.append(string)
            seen[string] = seen.get(string, 0) + 1
        
        for string in seen_list:
            if seen[string] == 1:
                k -= 1
            if k == 0:
                return string
        return ""