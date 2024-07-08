# 2442 - Number of Arithmetic Triplets
# Date: 2024-06-01
# Runtime: 45 ms, Memory: 16.4 MB
# Submission Id: 1273883760


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # nums[j] - nums[i] == nums[k] - nums[j] == diff
        # nums[k] = nums[j] + diff = nums[i] + 2 * diff

        counter = Counter()
        ans = 0
        for num in nums:
            counter[num] += 1
            ans += counter[num-diff] * counter[num-diff*2]
        return ans