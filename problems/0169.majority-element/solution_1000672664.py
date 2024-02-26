# 0169 - Majority Element
# Date: 2023-07-22
# Runtime: 163 ms, Memory: 17.9 MB
# Submission Id: 1000672664


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, major = 0, None
        for num in nums:
            if count == 0:
                major = num
            if num != major:
                count -= 1
            else:
                count += 1
        return major