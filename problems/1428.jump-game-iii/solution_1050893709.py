# 1428 - Jump Game III
# Date: 2023-09-16
# Runtime: 253 ms, Memory: 22.9 MB
# Submission Id: 1050893709


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        stack = [start]
        while stack:
            idx = stack.pop()
            if arr[idx] == 0:
                return True
            for next_idx in (idx - arr[idx], idx + arr[idx]):
                if 0 <= next_idx < n and arr[next_idx] >= 0:
                    stack.append(next_idx)
            arr[idx] = -1
        return False