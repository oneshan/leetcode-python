# 0514 - Freedom Trail
# Date: 2024-04-27
# Runtime: 232 ms, Memory: 17.8 MB
# Submission Id: 1243022052


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)

        queue = deque([(0, 0, len(key))])
        seen = {(0, 0)}
        while queue:
            for _ in range(len(queue)):
                ri, ki, step = queue.popleft()
                if ki == len(key):
                    return step
                if ring[ri] == key[ki]:
                    if (ri, ki+1) in seen:
                        continue
                    queue.append((ri, ki+1, step))
                    seen.add((ri, ki+1))
                else:
                    prev, nxt = ri-1, ri+1
                    if prev == -1: prev = n-1
                    if nxt == n: nxt = 0
                    if (prev, ki) not in seen:
                        queue.append((prev, ki, step+1))
                        seen.add((prev, ki))
                    if (nxt, ki) not in seen:
                        queue.append((nxt, ki, step+1))
                        seen.add((nxt, ki))
        return -1