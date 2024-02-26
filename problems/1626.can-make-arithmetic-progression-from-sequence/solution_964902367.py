# 1626 - Can Make Arithmetic Progression From Sequence
# Date: 2023-06-06
# Runtime: 53 ms, Memory: 16.5 MB
# Submission Id: 964902367


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True