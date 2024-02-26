# 3272 - Find the Grid of Region Average
# Date: 2024-02-05
# Runtime: 8485 ms, Memory: 35.4 MB
# Submission Id: 1166679207


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        len_r, len_c = len(image), len(image[0])
        
        def check(row, col):
            for r in range(3):
                for c in range(3):
                    curr_row, curr_col = row + r, col + c
                    for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                        adj_row, adj_col = curr_row + dr, curr_col + dc
                        if not row <= adj_row <= row + 2:
                            continue
                        if not col <= adj_col <= col + 2:
                            continue
                        if abs(image[curr_row][curr_col] - image[adj_row][adj_col]) > threshold:
                            return False
            return True

        value = [[0] * len_c for _ in range(len_r)]
        count = [[0] * len_c for _ in range(len_r)]
        for row in range(len_r-2):
            for col in range(len_c-2):
                if check(row, col):
                    avg = sum(image[row+r][col+c] for r in range(3) for c in range(3)) // 9
                    for r in range(3):
                        for c in range(3):
                            value[row+r][col+c] += avg
                            count[row+r][col+c] += 1

        for row in range(len_r):
            for col in range(len_c):
                if count[row][col] == 0:
                    value[row][col] = image[row][col]
                else:
                    value[row][col] //= count[row][col]
        return value