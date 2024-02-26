# 0322 - Coin Change
# Date: 2022-11-09
# Runtime: 1735 ms, Memory: 14.7 MB
# Submission Id: 839893673


from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(amount, 0)])
        seen = set()
        
        while queue:
            rem, count = queue.popleft()
            if rem == 0:
                return count
            for coin in coins:
                next_rem = rem - coin
                if next_rem >= 0 and next_rem not in seen:
                    seen.add(next_rem)
                    queue.append((next_rem, count+1))
        return -1