# 1428 - Jump Game III
# Date: 2022-10-25
# Runtime: 557 ms, Memory: 67 MB
# Submission Id: 829915970


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = - arr[start]
            return (self.canReach(arr, start + arr[start])
                    or self.canReach(arr, start - arr[start]))
        return False