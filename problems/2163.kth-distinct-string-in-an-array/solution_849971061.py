# 2163 - Kth Distinct String in an Array
# Date: 2022-11-26
# Runtime: 198 ms, Memory: 14.1 MB
# Submission Id: 849971061


from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)

        for string in arr:
            if counter[string] == 1:
                k -= 1
            if k == 0:
                return string
        return ''