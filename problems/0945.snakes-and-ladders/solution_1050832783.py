# 0945 - Snakes and Ladders
# Date: 2023-09-16
# Runtime: 108 ms, Memory: 16.4 MB
# Submission Id: 1050832783


from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target_idx = n ** 2
        board.reverse()
        
        queue = deque([1])
        visited = set()
        step = 0
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                for next_idx in range(idx+1, min(idx+6, target_idx) + 1):
                    r, c = divmod(next_idx-1, n)
                    if r & 1:
                        c = n-1-c
                    if board[r][c] != -1:
                        next_idx = board[r][c]
                    if next_idx == target_idx:
                        return step+1
                    if next_idx not in visited:
                        visited.add(next_idx)
                        queue.append(next_idx)
            step += 1
        return -1