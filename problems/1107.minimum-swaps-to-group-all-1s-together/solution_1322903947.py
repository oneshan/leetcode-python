# 1107 - Minimum Swaps to Group All 1's Together
# Date: 2024-07-16
# Runtime: 550 ms, Memory: 19.5 MB
# Submission Id: 1322903947


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)

        count = 0
        for i in range(ones):
            count += data[i]

        ans = ones-count
        for i in range(ones, len(data)):
            count -= data[i-ones]
            count += data[i]
            ans = min(ans, ones-count)
        return ans            