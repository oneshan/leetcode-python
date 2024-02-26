# 0984 - Most Stones Removed with Same Row or Column
# Date: 2022-11-15
# Runtime: 354 ms, Memory: 14.6 MB
# Submission Id: 843926347


from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        same_row, same_col = defaultdict(list), defaultdict(list)
        for idx, (row, col) in enumerate(stones):
            same_row[row].append(idx)
            same_col[col].append(idx)
        
        seen = set()
        removed = 0
        for idx in range(n):
            if idx in seen:
                removed += 1
                continue
            stack = [idx]
            while stack:
                idx = stack.pop()
                for next_idx in same_row[stones[idx][0]]:
                    if next_idx not in seen:
                        seen.add(next_idx)
                        stack.append(next_idx)
                for next_idx in same_col[stones[idx][1]]:
                    if next_idx not in seen:
                        seen.add(next_idx)
                        stack.append(next_idx)
        return removed