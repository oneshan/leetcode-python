# 0217 - Contains Duplicate
# Date: 2022-07-16
# Runtime: 994 ms, Memory: 26 MB
# Submission Id: 748349680


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False