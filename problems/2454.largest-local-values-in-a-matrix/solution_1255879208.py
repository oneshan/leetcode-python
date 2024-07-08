# 2454 - Largest Local Values in a Matrix
# Date: 2024-05-12
# Runtime: 108 ms, Memory: 17.2 MB
# Submission Id: 1255879208


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        len_r = len_c = len(grid)

        ans = [[0] * (len_c-2) for _ in range(len_r-2)]
        temp = defaultdict(list)

        for r in range(len_r):
            queue = deque()
            for c in range(len_c):
                while queue and grid[r][queue[-1]] < grid[r][c]:
                    queue.pop()
                queue.append(c)
                if c - queue[0] >= 3:
                    queue.popleft()
                if c >= 2:
                    temp[r].append(grid[r][queue[0]])

        for c in range(len_c-2):
            queue = deque()
            for r in range(len_r):
                while queue and temp[queue[-1]][c] < temp[r][c]:
                    queue.pop()
                queue.append(r)
                if r - queue[0] >= 3:
                    queue.popleft()
                if r >= 2:
                    ans[r-2][c] = temp[queue[0]][c]

        return ans