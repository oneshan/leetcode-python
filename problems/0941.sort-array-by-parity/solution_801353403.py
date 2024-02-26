# 0941 - Sort Array By Parity
# Date: 2022-09-16
# Runtime: 157 ms, Memory: 14.7 MB
# Submission Id: 801353403


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums)-1
        
        idx = 0
        while even < odd:
            if nums[idx] & 1:
                nums[idx], nums[odd] = nums[odd], nums[idx]
                odd -= 1
            else:
                idx += 1
                even += 1
        return nums