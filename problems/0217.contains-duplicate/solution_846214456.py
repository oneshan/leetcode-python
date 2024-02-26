# 0217 - Contains Duplicate
# Date: 2022-11-19
# Runtime: 609 ms, Memory: 26 MB
# Submission Id: 846214456


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False