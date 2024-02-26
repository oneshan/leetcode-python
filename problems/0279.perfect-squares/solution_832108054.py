# 0279 - Perfect Squares
# Date: 2022-10-28
# Runtime: 861 ms, Memory: 15.2 MB
# Submission Id: 832108054


from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        perfect = [i*i for i in range(1, int(n**0.5)+1)]
        if n in perfect:
            return 1

        queue = deque([(n, 0)])
        seen = set()
        while queue:
            n, step = queue.popleft()
            for num in perfect:
                next_n = n - num
                if next_n == 0:
                    return step+1
                if next_n < 0:
                    break
                if next_n not in seen:
                    queue.append((next_n, step+1))
                    seen.add(next_n)
        return -1