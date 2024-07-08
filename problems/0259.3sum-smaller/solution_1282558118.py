# 0259 - 3Sum Smaller
# Date: 2024-06-09
# Runtime: 684 ms, Memory: 16.7 MB
# Submission Id: 1282558118


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        ans = 0
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum < target:
                    ans += k-j
                    j += 1
                else:
                    k -= 1
        return ans