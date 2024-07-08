# 0719 - Find K-th Smallest Pair Distance
# Date: 2024-06-16
# Runtime: 92 ms, Memory: 17.3 MB
# Submission Id: 1290235369


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def check(dist):
            count = i = j = 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= dist:
                    j += 1
                i += 1
                count += j - i
            return count >= k

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left