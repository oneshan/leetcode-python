# 0554 - Brick Wall
# Date: 2024-05-26
# Runtime: 154 ms, Memory: 21.5 MB
# Submission Id: 1268302121


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counter = Counter()
        for bricks in wall:
            curr = 0
            for i in range(len(bricks)-1):
                curr += bricks[i]
                counter[curr] += 1

        if not counter:
            return len(wall)
        return len(wall) - max(counter.values())