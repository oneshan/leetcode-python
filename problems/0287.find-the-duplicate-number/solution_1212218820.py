# 0287 - Find the Duplicate Number
# Date: 2024-03-24
# Runtime: 455 ms, Memory: 30.5 MB
# Submission Id: 1212218820


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast