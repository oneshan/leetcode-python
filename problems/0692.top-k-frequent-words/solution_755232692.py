# 0692 - Top K Frequent Words
# Date: 2022-07-24
# Runtime: 139 ms, Memory: 14 MB
# Submission Id: 755232692


import heapq

class FreqWord:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return lt(self.freq, other.freq)
        else:
            return lt(other.word, self.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        
        h = []
        for key, value in counter.items():
            heapq.heappush(h, FreqWord(value, key))
            if len(h) > k:
                heapq.heappop(h)
        
        return [heapq.heappop(h).word for _ in range(k)][::-1]