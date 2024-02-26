# 0836 - Race Car
# Date: 2022-10-10
# Runtime: 68 ms, Memory: 14.3 MB
# Submission Id: 819388291


from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)])  # steps, position, speed
        while queue:
            steps, pos, speed = queue.popleft()
            if pos == target:
                return steps

            queue.append((steps+1, pos+speed, speed*2)) # 'A'
            # 'R' reverse if passed the target and speed is postive 
            if speed > 0 and pos + speed > target:
                queue.append((steps+1, pos, -1))
            # 'R' reverse if did not pass the target and speed is negative 
            if speed < 0 and pos + speed < target:
                queue.append((steps+1, pos, 1))