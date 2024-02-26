# 1391 - Counting Elements
# Date: 2023-08-22
# Runtime: 36 ms, Memory: 16.4 MB
# Submission Id: 1028357829


from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = 0
        for num in counter:
            if counter[num+1]:
                ans += counter[num]
        return ans