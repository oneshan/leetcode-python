# 0015 - 3Sum
# Date: 2022-10-18
# Runtime: 2061 ms, Memory: 18 MB
# Submission Id: 825157499


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
                
    def two_sum(self, nums, i):  # O(N)
        left, right = i+1, len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                self.ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1