# 0692 - Top K Frequent Words
# Date: 2022-07-24
# Runtime: 95 ms, Memory: 14 MB
# Submission Id: 755228082


import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        
        h = []
        for key, value in counter.items():
            heapq.heappush(h, (-value, key))
        
        return [heapq.heappop(h)[1] for _ in range(k)]