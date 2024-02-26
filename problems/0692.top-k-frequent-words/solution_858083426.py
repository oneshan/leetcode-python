# 0692 - Top K Frequent Words
# Date: 2022-12-11
# Runtime: 56 ms, Memory: 14.1 MB
# Submission Id: 858083426


from collections import Counter
import heapq

class WordFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        
        top_k = []
        for word, count in counter.items():
            heapq.heappush(top_k, WordFreq(word, count))
            if len(top_k) > k:
                heapq.heappop(top_k)
        return [item.word for item in sorted(top_k, reverse=True)]