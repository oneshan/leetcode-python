# 0748 - Largest Number At Least Twice of Others
# Date: 2022-07-13
# Runtime: 42 ms, Memory: 13.9 MB
# Submission Id: 745659678


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        
        max_num = sec_num = 0
        max_idx = -1
        for idx, num in enumerate(nums):
            if not max_num or num >= max_num:
                max_num, sec_num = num, max_num
                max_idx = idx
            elif not sec_num or num >= sec_num:
                sec_num = num
        return max_idx if max_num >= sec_num * 2 else -1