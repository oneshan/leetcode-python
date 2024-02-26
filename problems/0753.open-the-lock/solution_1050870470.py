# 0753 - Open the Lock
# Date: 2023-09-16
# Runtime: 458 ms, Memory: 17.7 MB
# Submission Id: 1050870470


from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if '0000' in seen:
            return -1
        
        queue = deque(['0000'])
        step = 0
        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                if num == target:
                    return step
                for i in range(4):
                    digit = int(num[i])
                    for d in (-1, 1):
                        next_d = (digit + d) % 10
                        next_num = num[:i] + str(next_d) + num[i+1:]
                        if next_num not in seen:
                            queue.append(next_num)
                            seen.add(next_num)
            step += 1
        return -1