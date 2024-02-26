# 1839 - Decode XORed Array
# Date: 2022-10-15
# Runtime: 565 ms, Memory: 15.9 MB
# Submission Id: 822965678


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        ans = [0] * (n + 1)
        ans[0] = first
        for i in range(n):
            ans[i+1] = encoded[i] ^ ans[i]
        return ans