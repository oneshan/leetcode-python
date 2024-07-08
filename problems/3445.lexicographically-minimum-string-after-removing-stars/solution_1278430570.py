# 3445 - Lexicographically Minimum String After Removing Stars
# Date: 2024-06-05
# Runtime: 595 ms, Memory: 28.5 MB
# Submission Id: 1278430570


class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        list_s = list(s)

        for idx, ch in enumerate(s):
            if ch != '*':
                heapq.heappush(heap, (ch, -idx))
            else:
                list_s[idx] = ''
                c, i = heapq.heappop(heap)
                list_s[-i] = ''

        return ''.join(list_s)