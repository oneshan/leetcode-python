# 1839 - Decode XORed Array
# Date: 2022-10-15
# Runtime: 652 ms, Memory: 16 MB
# Submission Id: 822965199


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        ans = [0] * (n + 1)
        ans[0] = first
        for i in range(n):
            first ^= encoded[i]
            ans[i+1] = first
        return ans