# 0966 - Binary Subarrays With Sum
# Date: 2024-05-31
# Runtime: 209 ms, Memory: 20.5 MB
# Submission Id: 1273354210


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1

        ans = curr = 0
        for num in nums:
            curr += num
            ans += counter[curr-goal]
            counter[curr] += 1
        return ans