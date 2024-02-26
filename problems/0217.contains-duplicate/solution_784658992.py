# 0217 - Contains Duplicate
# Date: 2022-08-27
# Runtime: 700 ms, Memory: 26 MB
# Submission Id: 784658992


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False