# 0189 - Rotate Array
# Date: 2023-07-24
# Runtime: 240 ms, Memory: 27.8 MB
# Submission Id: 1002629060


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start_idx = 0
        while count < n:
            idx, prev = start_idx, nums[start_idx]
            while True:
                idx = (idx + k) % n
                prev, nums[idx] = nums[idx], prev
                count += 1
                if idx == start_idx:
                    break
            start_idx += 1