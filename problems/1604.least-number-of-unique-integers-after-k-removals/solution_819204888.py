# 1604 - Least Number of Unique Integers after K Removals
# Date: 2022-10-10
# Runtime: 630 ms, Memory: 35 MB
# Submission Id: 819204888


from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = defaultdict(int)
        for num in arr:
            counter[num] += 1
        
        uniques = len(counter)
        for freq, num in sorted([(freq, num) for num, freq in counter.items()]):
            if freq <= k:
                k -= freq
                uniques -= 1
            else:
                break
        return uniques
        