# 0169 - Majority Element
# Date: 2024-02-12
# Runtime: 131 ms, Memory: 18 MB
# Submission Id: 1172705201


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0
        for num in nums:
            if count == 0:
                ans = num
            count += (1 if ans == num else -1)
        return ans