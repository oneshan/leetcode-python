# 0958 - Sort Array By Parity II
# Date: 2022-11-17
# Runtime: 444 ms, Memory: 16.2 MB
# Submission Id: 845179132


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_idx, odd_idx = 0, 1
        while even_idx < n and odd_idx < n:
            if nums[even_idx] & 1:
                while odd_idx < n and nums[odd_idx] & 1:
                    odd_idx += 2
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            even_idx += 2
        return nums