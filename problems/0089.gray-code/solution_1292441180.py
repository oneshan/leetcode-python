# 0089 - Gray Code
# Date: 2024-06-18
# Runtime: 78 ms, Memory: 24 MB
# Submission Id: 1292441180


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        for i in range(1 << n):
            num = i ^ (i >> 1)
            ans.append(num)
        return ans