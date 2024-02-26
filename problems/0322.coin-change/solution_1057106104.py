# 0322 - Coin Change
# Date: 2023-09-23
# Runtime: 430 ms, Memory: 17 MB
# Submission Id: 1057106104


from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([0])
        seen = set()
        ans = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == amount:
                    return ans
                for coin in coins:
                    next_c = coin + curr
                    if next_c <= amount and next_c not in seen:
                        seen.add(next_c)
                        queue.append(next_c)
            ans += 1
        return -1