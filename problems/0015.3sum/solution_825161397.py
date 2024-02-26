# 0015 - 3Sum
# Date: 2022-10-18
# Runtime: 978 ms, Memory: 18.2 MB
# Submission Id: 825161397


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()  # O(NlogN)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.two_sum(nums, i)
        return self.ans
                
    def two_sum(self, nums, i):  # Time: O(N), Space: O(N)
        seen = set()
        idx = i + 1
        while idx < len(nums):
            complement = -nums[i] - nums[idx]
            if complement in seen:
                self.ans.append([nums[i], nums[idx], complement])
                while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                    idx += 1
            seen.add(nums[idx])
            idx += 1