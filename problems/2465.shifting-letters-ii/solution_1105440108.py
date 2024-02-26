# 2465 - Shifting Letters II
# Date: 2023-11-24
# Runtime: 1495 ms, Memory: 42.2 MB
# Submission Id: 1105440108


import heapq

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        
        heap = []
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            heapq.heappush(heap, (start, delta))
            heapq.heappush(heap, (end+1, -delta))

        ans = []
        curr = 0
        for i in range(n):
            while heap and heap[0][0] == i:
                _, delta = heapq.heappop(heap)
                curr += delta
            diff = (ord(s[i]) - ord('a') + curr) % 26
            ans.append(chr(ord('a') + diff))

        return ''.join(ans)