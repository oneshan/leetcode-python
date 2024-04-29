# 0753 - Open the Lock
# Date: 2024-04-22
# Runtime: 276 ms, Memory: 18.3 MB
# Submission Id: 1238755272


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target = tuple(int(d) for d in target)
        seen = {tuple(int(d) for d in deadend) for deadend in deadends}

        if (0, 0, 0 ,0) in seen:
            return -1
            
        queue = deque([(0, 0, 0, 0)])
        step = 0
        while queue:
            for _ in range(len(queue)):
                state = queue.popleft()
                if state == target:
                    return step
                for i in range(4):
                    for dx in (1, -1):
                        next_state = list(state)
                        next_state[i] = (next_state[i] + dx) % 10
                        next_state = tuple(next_state)
                        if next_state not in seen:
                            seen.add(next_state)
                            queue.append(next_state)
            step += 1
        return -1