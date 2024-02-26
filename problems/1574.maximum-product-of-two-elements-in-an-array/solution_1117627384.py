# 1574 - Maximum Product of Two Elements in an Array
# Date: 2023-12-12
# Runtime: 54 ms, Memory: 16.5 MB
# Submission Id: 1117627384


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = 0
        for num in nums:
            if num > m1:
                m1, m2 = num, m1
            elif num > m2:
                m1, m2 = m1, num
        return (m1-1) * (m2-1)