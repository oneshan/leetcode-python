# 0753 - Open the Lock
# Date: 2022-10-25
# Runtime: 855 ms, Memory: 15.3 MB
# Submission Id: 829998831


from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        digits = '0123456789'

        seen = set(deadends)
        if '0000' in seen:
            return -1
        
        queue = deque([('0000', 0)])
        while queue:
            num, step = queue.popleft()
            if num == target:
                return step
            for i in range(4):
                next_num = num[:i] + digits[(int(num[i])+1) % 10] + num[i+1:]
                prev_num = num[:i] + digits[(int(num[i])-1) % 10] + num[i+1:]
                if next_num not in seen:
                    queue.append((next_num, step+1))
                    seen.add(next_num)
                if prev_num not in seen:
                    queue.append((prev_num, step+1))
                    seen.add(prev_num)
        return -1