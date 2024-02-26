# 1428 - Jump Game III
# Date: 2022-10-25
# Runtime: 555 ms, Memory: 20.5 MB
# Submission Id: 829912594


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = {start}
        stack = [start]
        while stack:
            idx = stack.pop()
            if arr[idx] == 0:
                return True
            for next_idx in (idx - arr[idx], idx + arr[idx]):
                if next_idx not in seen and 0 <= next_idx < n:
                    stack.append(next_idx)
                    seen.add(next_idx)
        return False