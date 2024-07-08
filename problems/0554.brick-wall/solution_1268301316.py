# 0554 - Brick Wall
# Date: 2024-05-26
# Runtime: 164 ms, Memory: 21.6 MB
# Submission Id: 1268301316


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counter = Counter()
        for bricks in wall:
            curr = 0
            n = len(bricks)
            for brick in bricks:
                curr += brick
                counter[curr] += 1

        counter.pop(sum(wall[0]))
        if not counter:
            return len(wall)
        return len(wall) - max(counter.values())