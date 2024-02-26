# 1391 - Counting Elements
# Date: 2023-08-22
# Runtime: 42 ms, Memory: 16.3 MB
# Submission Id: 1028358582


from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = 0
        for num in counter:
            ans += counter[num-1]
        return ans