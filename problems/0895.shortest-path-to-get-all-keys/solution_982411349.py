# 0895 - Shortest Path to Get All Keys
# Date: 2023-06-29
# Runtime: 270 ms, Memory: 19.9 MB
# Submission Id: 982411349


from collections import deque, defaultdict

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        len_r, len_c = len(grid), len(grid[0])
        
        queue = deque()  # [row, col, key_state, distance]
        seen = defaultdict(set)

        key_set, lock_set = set(), set()
        all_keys = 0
        for r in range(len_r):
            for c in range(len_c):
                ch = grid[r][c]
                if ch in 'abcdef':
                    key_set.add(grid[r][c])
                    all_keys |= 1 << (ord(ch) - ord('a'))
                elif ch in 'ABCDEF':
                    lock_set.add(grid[r][c])
                elif ch == '@':
                    queue.append((r, c, 0, 0))
                    seen[0].add((r, c))  
                    
        while queue:
            r, c, keys, dist = queue.popleft()
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                next_r, next_c = r + dr, c + dc
                if 0 <= next_r < len_r and 0 <= next_c < len_c and grid[next_r][next_c] != '#':
                    ch = grid[next_r][next_c]
                    if ch in lock_set and (1 << (ord(ch) - ord('A'))) & keys == 0:
                        continue
                    elif ch in key_set and (1 << (ord(ch) - ord('a'))) & keys == 0:
                        new_keys = keys | (1 << (ord(ch) - ord('a')))
                        if new_keys == all_keys:
                            return dist + 1
                        seen[new_keys].add((next_r, next_c))
                        queue.append((next_r, next_c, new_keys, dist+1))
                    elif (next_r, next_c) not in seen[keys]:
                        seen[keys].add((next_r, next_c))
                        queue.append((next_r, next_c, keys, dist+1))
        return -1