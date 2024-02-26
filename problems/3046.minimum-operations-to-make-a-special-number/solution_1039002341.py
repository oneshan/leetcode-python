# 3046 - Minimum Operations to Make a Special Number
# Date: 2023-09-03
# Runtime: 37 ms, Memory: 16.2 MB
# Submission Id: 1039002341


class Solution:
    def minimumOperations(self, num: str) -> int:
        # 25, 50, 75, 00
        n = len(num)
        
        count, has0, has5 = 0, 0, 0
        for i in range(n-1, -1, -1):
            if has0 and num[i] in '50':
                return n - i - 2
            if not has0 and num[i] == '0':
                has0 = True

            if has5 and num[i] in '27':
                return n - i - 2
            if not has5 and num[i] == '5':
                has5 = True

        return n - int(has0)