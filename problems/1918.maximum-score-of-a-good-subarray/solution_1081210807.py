# 1918 - Maximum Score of a Good Subarray
# Date: 2023-10-22
# Runtime: 1021 ms, Memory: 26.7 MB
# Submission Id: 1081210807


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = k
        ans = curr_min = nums[k]
        while left > 0 or right < n-1:
            if left == 0:
                right += 1
            elif right == n-1:
                left -= 1
            elif nums[left-1] < nums[right+1]:
                right += 1
            else:
                left -= 1
            curr_min = min(curr_min, nums[left], nums[right])
            ans = max(ans, curr_min * (right - left + 1))
        return ans