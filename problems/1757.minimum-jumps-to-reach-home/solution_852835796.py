# 1757 - Minimum Jumps to Reach Home
# Date: 2022-12-01
# Runtime: 103 ms, Memory: 14.7 MB
# Submission Id: 852835796


from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        seen = set()
        queue = deque([(0, 0, False)])
        
        upper_bound = max(max(forbidden), x) + a + b
        
        while queue:
            node, step, is_prev_b = queue.popleft()
            if node == x:
                return step
            
            nxt_a, nxt_b = node+a, node-b
            if nxt_a <= upper_bound and nxt_a not in forbidden and (nxt_a, False) not in seen:
                seen.add((nxt_a, False))
                queue.append((nxt_a, step+1, False))
            if nxt_b > 0 and nxt_b not in forbidden and not is_prev_b and (nxt_b, True) not in seen:
                seen.add((nxt_b, True))
                queue.append((nxt_b, step+1, True))
        return -1