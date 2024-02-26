# 1428 - Jump Game III
# Date: 2023-09-16
# Runtime: 270 ms, Memory: 23.1 MB
# Submission Id: 1050893046


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        stack = [start]
        seen = {start}
        while stack:
            idx = stack.pop()
            if arr[idx] == 0:
                return True
            for next_idx in (idx - arr[idx], idx + arr[idx]):
                if 0 <= next_idx < n and next_idx not in seen:
                    stack.append(next_idx)
                    seen.add(next_idx)
        return False