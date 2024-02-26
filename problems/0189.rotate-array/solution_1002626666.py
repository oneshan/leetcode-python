# 0189 - Rotate Array
# Date: 2023-07-24
# Runtime: 250 ms, Memory: 27.9 MB
# Submission Id: 1002626666


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start_idx = curr_idx = 0
        while count < n:
            curr_idx = start_idx
            prev = nums[curr_idx]
            
            while True:
                curr_idx = (curr_idx + k) % n
                prev, nums[curr_idx] = nums[curr_idx], prev
                count += 1
                if curr_idx == start_idx:
                    start_idx += 1
                    break