# 1428 - Jump Game III
# Date: 2022-10-25
# Runtime: 314 ms, Memory: 20.8 MB
# Submission Id: 829914581


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        stack = [start]
        while stack:
            idx = stack.pop()
            if arr[idx] == 0:
                return True
            if arr[idx] < 0:
                continue
            for next_idx in (idx - arr[idx], idx + arr[idx]):
                if 0 <= next_idx < n:
                    stack.append(next_idx)
            arr[idx] = -1
        return False