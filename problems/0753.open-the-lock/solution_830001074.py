# 0753 - Open the Lock
# Date: 2022-10-25
# Runtime: 1541 ms, Memory: 15.4 MB
# Submission Id: 830001074


from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if '0000' in seen:
            return -1
        
        queue = deque([('0000', 0)])
        while queue:
            num, step = queue.popleft()
            if num == target:
                return step
            for i in range(4):
                digit = int(num[i])
                for d in (-1, 1):
                    next_digit = (digit+d) % 10
                    next_num = num[:i] + str(next_digit) + num[i+1:]
                    if next_num not in seen:
                        queue.append((next_num, step+1))
                        seen.add(next_num)
        return -1