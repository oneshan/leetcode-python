# 2846 - Robot Collisions
# Date: 2024-07-13
# Runtime: 912 ms, Memory: 34.2 MB
# Submission Id: 1319252607


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        indices = list(range(n))
        indices.sort(key=lambda x: positions[x])
        
        to_right = []
        for idx in indices:
            if directions[idx] == 'R':
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