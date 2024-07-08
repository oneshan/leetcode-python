# 1951 - Find the Winner of the Circular Game
# Date: 2024-07-08
# Runtime: 122 ms, Memory: 16.5 MB
# Submission Id: 1313598502


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1, n+1))
        ans = 0
        while queue:
            for _ in range(k-1):
                p = queue.popleft()
                queue.append(p)
            ans = queue.popleft()
        return ans