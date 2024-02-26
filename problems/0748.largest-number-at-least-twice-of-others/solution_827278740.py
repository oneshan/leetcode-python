# 0748 - Largest Number At Least Twice of Others
# Date: 2022-10-21
# Runtime: 74 ms, Memory: 13.9 MB
# Submission Id: 827278740


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = sec_num = max_idx = -1
        for idx, num in enumerate(nums):
            if max_num == -1 or num >= max_num:
                max_idx, max_num, sec_num = idx, num, max_num
            elif sec_num == -1 or num >= sec_num:
                sec_num = num
        return max_idx if max_num >= sec_num * 2 else -1