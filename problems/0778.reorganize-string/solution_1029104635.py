# 0778 - Reorganize String
# Date: 2023-08-23
# Runtime: 44 ms, Memory: 16.3 MB
# Submission Id: 1029104635


from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = Counter(s)
        pq = [(-count, ch) for ch, count in counter.items()]
        heapq.heapify(pq)
        
        ans = []
        while pq:
            count1, ch1= heapq.heappop(pq)
            if not ans or ch1 != ans[-1]:
                ans.append(ch1)
                if count1 + 1 != 0:
                    heapq.heappush(pq, (count1+1, ch1))
            else:
                if not pq:
                    return ''
                count2, ch2 = heapq.heappop(pq)
                ans.append(ch2)
                if count2 + 1 != 0:
                    heapq.heappush(pq, (count2+1, ch2))
                heapq.heappush(pq, (count1, ch1))
        return ''.join(ans)