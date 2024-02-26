# 1626 - Can Make Arithmetic Progression From Sequence
# Date: 2022-11-12
# Runtime: 82 ms, Memory: 14 MB
# Submission Id: 841737087


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True