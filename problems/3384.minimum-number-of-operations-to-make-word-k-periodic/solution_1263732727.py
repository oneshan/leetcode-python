# 3384 - Minimum Number of Operations to Make Word K-Periodic
# Date: 2024-05-21
# Runtime: 136 ms, Memory: 18.8 MB
# Submission Id: 1263732727


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        
        counter = Counter()
        for i in range(0, n, k):
            counter[word[i:i+k]] += 1        
        return (n // k) - max(counter.values())