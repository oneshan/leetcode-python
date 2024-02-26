# 1319 - Unique Number of Occurrences
# Date: 2022-10-14
# Runtime: 74 ms, Memory: 14.1 MB
# Submission Id: 822206749


from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)
        for num in arr:
            counter[num] += 1
        
        return len(counter) == len(set(counter.values()))