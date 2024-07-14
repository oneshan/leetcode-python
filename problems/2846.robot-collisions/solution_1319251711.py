# 2846 - Robot Collisions
# Date: 2024-07-13
# Runtime: 1141 ms, Memory: 39.2 MB
# Submission Id: 1319251711


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        heap = []
        for idx, (pos, d) in enumerate(zip(positions, directions)):
            heapq.heappush(heap, (pos, d, idx))
        
        to_right = []
        while heap:
            pos, d, idx = heapq.heappop(heap)
            if d == 'R':
                to_right.append(idx)
                continue
            
            while to_right and healths[idx]:
                if healths[to_right[-1]] > healths[idx]:
                    healths[to_right[-1]] -= 1
                    healths[idx] = 0
                    break
                elif healths[to_right[-1]] == healths[idx]:
                    healths[idx] = healths[to_right.pop()] = 0
                else:
                    healths[idx] -= 1
                    healths[to_right.pop()] = 0
        
        return [health for health in healths if health]