# 0945 - Snakes and Ladders
# Date: 2024-06-06
# Runtime: 103 ms, Memory: 16.5 MB
# Submission Id: 1279603117


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        len_r, len_c = len(board), len(board[0])
        target = len_r * len_c

        def idx2rc(idx):
            r, c = divmod(idx-1, len_c)
            if r & 1:
                c = len_c - 1 - c            
            r = len_r - 1 - r
            return r, c

        queue = deque([1])
        seen = set()
        step = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                        return step

                for next_idx in range(curr+1, min(curr+6, target)+1):
                    r, c = idx2rc(next_idx)
                    if board[r][c] != -1:
                        next_idx = board[r][c]
                    if next_idx in seen:
                        continue
                    seen.add(next_idx)
                    queue.append(next_idx)
            step += 1

        return -1