# 0753 - Open the Lock
# Date: 2023-09-16
# Runtime: 477 ms, Memory: 17.5 MB
# Submission Id: 1050877802


from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(num for num in deadends)
        
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
                    for d in (-1, 1):
                        next_d = str((int(num[i]) + d) % 10)
                        next_num = num[:i] + next_d + num[i+1:]
                        if next_num not in seen:
                            seen.add(next_num)
                            queue.append(next_num)
            step += 1
        return -1