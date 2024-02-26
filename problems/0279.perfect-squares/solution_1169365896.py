# 0279 - Perfect Squares
# Date: 2024-02-08
# Runtime: 523 ms, Memory: 223.8 MB
# Submission Id: 1169365896


class Solution:
    def numSquares(self, n: int) -> int:
        square = [i * i for i in range(0, 101)]


        queue = deque([n])
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                value = queue.popleft()
                for s in square:
                    if value == s:
                        return ans
                    if value < s:
                        break
                    queue.append(value-s)