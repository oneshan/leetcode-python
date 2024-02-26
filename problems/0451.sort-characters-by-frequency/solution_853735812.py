# 0451 - Sort Characters By Frequency
# Date: 2022-12-03
# Runtime: 80 ms, Memory: 15.4 MB
# Submission Id: 853735812


from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        heap = [(-count, ch) for ch, count in counter.items()]
        heapq.heapify(heap)
        
        string_builder = []
        while heap:
            count, ch = heapq.heappop(heap)
            string_builder.append(ch * -count)
        return ''.join(string_builder)