# 0945 - Snakes and Ladders
# Date: 2023-01-24
# Runtime: 338 ms, Memory: 14 MB
# Submission Id: 884395024


from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target_idx = n ** 2
        board.reverse()
        
        queue = deque([[1, 0]])
        visited = set()
        while queue:
            idx, step = queue.popleft()
            if idx == target_idx:
                return step
            for next_idx in range(idx+1, min(idx+6, target_idx)+1):
                r, c = divmod(next_idx-1, n)
                if r & 1:
                    c = n-1-c
                if board[r][c] != -1:
                    next_idx = board[r][c]
                if next_idx not in visited:
                    visited.add(next_idx)
                    queue.append([next_idx, step+1])
        return -1