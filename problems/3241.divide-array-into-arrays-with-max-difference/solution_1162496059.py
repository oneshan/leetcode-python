# 3241 - Divide Array Into Arrays With Max Difference
# Date: 2024-02-01
# Runtime: 704 ms, Memory: 30.8 MB
# Submission Id: 1162496059


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        ans = []
        for i in range(0, n, 3):
            if nums[i+2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i+1], nums[i+2]])
        return ans