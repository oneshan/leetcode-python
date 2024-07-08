# 0880 - Rectangle Area II
# Date: 2024-06-17
# Runtime: 72 ms, Memory: 16.4 MB
# Submission Id: 1291160325


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 1_000_000_007
        ans = 0

        OPEN, CLOSE = 1, -1
        x_set = set()
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, OPEN))
            events.append((y2, x1, x2, CLOSE))
            x_set.add(x1)
            x_set.add(x2)
        events.sort()

        x_list = sorted(x_set)
        x_idx = {x: idx for idx, x in enumerate(x_list)}
        count = [0] * len(x_list)

        prev_y = 0
        for y1, x1, x2, sign in events:

            for i in range(len(x_list)):
                if count[i]:
                    ans += (x_list[i+1] - x_list[i]) * (y1 - prev_y)
            
            for i in range(x_idx[x1], x_idx[x2]):
                count[i] += sign

            prev_y = y1

        return ans % MOD