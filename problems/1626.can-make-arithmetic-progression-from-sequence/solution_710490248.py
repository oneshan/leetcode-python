# 1626 - Can Make Arithmetic Progression From Sequence
# Date: 2022-05-30
# Runtime: 63 ms, Memory: 13.9 MB
# Submission Id: 710490248


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True