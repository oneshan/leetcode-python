# 3508 - Number of Bit Changes to Make Two Integers Equal
# Date: 2024-07-21
# Runtime: 40 ms, Memory: 16.4 MB
# Submission Id: 1327893916


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        for i in range(32):
            if n & 1 and k & 1 == 0:
                ans += 1
            if n & 1 == 0 and k & 1:
                return -1

            n >>= 1
            k >>= 1
        return ans