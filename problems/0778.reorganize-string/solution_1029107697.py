# 0778 - Reorganize String
# Date: 2023-08-23
# Runtime: 40 ms, Memory: 16.3 MB
# Submission Id: 1029107697


from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = Counter(s)
        pq = [(-count, ch) for ch, count in counter.items()]
        heapq.heapify(pq)
        
        if -pq[0][0] > (n+1) // 2:
            return ''
        
        ans = [''] * n
        idx = 0
        while pq:
            count, ch = heapq.heappop(pq)
            for i in range(-count):
                ans[idx] = ch
                idx += 2
                if idx >= n:
                    idx = 1
        return ''.join(ans)