# 1604 - Least Number of Unique Integers after K Removals
# Date: 2023-09-17
# Runtime: 341 ms, Memory: 33.3 MB
# Submission Id: 1051659898


from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        
        freq = sorted(list(counter.values()))
        ans = len(counter)
        for f in freq:
            if f > k:
                break
            k -= f
            ans -= 1
        return ans