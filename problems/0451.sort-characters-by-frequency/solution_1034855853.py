# 0451 - Sort Characters By Frequency
# Date: 2023-08-29
# Runtime: 47 ms, Memory: 17.5 MB
# Submission Id: 1034855853


from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        arr = [(-count, ch) for ch, count in counter.items()]
        heapq.heapify(arr)
        
        ans = []
        while arr:
            count, ch = heapq.heappop(arr)
            ans.append(ch * -count)
        return ''.join(ans)