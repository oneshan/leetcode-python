# 0079 - Word Search
# Date: 2024-03-01
# Runtime: 3961 ms, Memory: 19.4 MB
# Submission Id: 1190376043


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_r, len_c = len(board), len(board[0])

        def check(r, c):
            queue = deque([(r, c, 1 << (r*len_c+c))])
            for i in range(1, len(word)):
                for _ in range(len(queue)):
                    r, c, seen = queue.popleft()
                    for nr, nc in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
                        if 0 <= nr < len_r and 0 <= nc < len_c and board[nr][nc] == word[i]:
                            mask = 1 << (nr * len_c + nc)
                            if mask & seen == 0:
                                queue.append((nr, nc, seen | mask ))
                if not queue:
                    return False
            return True


        for r in range(len_r):
            for c in range(len_c):
                if board[r][c] == word[0] and check(r, c):
                    return True
        return False