# 0880 - Rectangle Area II
# Date: 2024-06-17
# Runtime: 72 ms, Memory: 16.5 MB
# Submission Id: 1291141633


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 1_000_000_007
        ans = 0

        OPEN, CLOSE = 1, -1
        x_set = set()
        heap = []
        for x1, y1, x2, y2 in rectangles:
            heapq.heappush(heap, (y1, x1, x2, OPEN))
            heapq.heappush(heap, (y2, x1, x2, CLOSE))
            x_set.add(x1)
            x_set.add(x2)

        x_list = sorted(x_set)
        x_idx = {x: idx for idx, x in enumerate(x_list)}
        count = [0] * len(x_list)

        prev_y = heap[0][0]
        while heap:
            curr_y = heap[0][0]
            for i in range(len(x_list)):
                if count[i]:
                    ans += (x_list[i+1] - x_list[i]) * (curr_y - prev_y)
            
            while heap and heap[0][0] == curr_y:
                _, x1, x2, sign = heapq.heappop(heap)
                for i in range(x_idx[x1], x_idx[x2]):
                    count[i] += sign

            prev_y = curr_y

        return ans % MOD