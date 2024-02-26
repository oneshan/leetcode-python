# 0941 - Sort Array By Parity
# Date: 2023-09-28
# Runtime: 78 ms, Memory: 17.2 MB
# Submission Id: 1061230124


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_idx, odd_idx = 0, n-1
        while even_idx < odd_idx:
            if nums[even_idx] & 1 == 0:
                even_idx += 1
            else:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                odd_idx -= 1
        return nums