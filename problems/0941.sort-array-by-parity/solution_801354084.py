# 0941 - Sort Array By Parity
# Date: 2022-09-16
# Runtime: 182 ms, Memory: 14.8 MB
# Submission Id: 801354084


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = len(nums)-1
        
        idx = 0
        while idx < odd:
            if nums[idx] & 1:
                nums[idx], nums[odd] = nums[odd], nums[idx]
                odd -= 1
            else:
                idx += 1
        return nums