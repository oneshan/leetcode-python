# 3241 - Divide Array Into Arrays With Max Difference
# Date: 2023-12-17
# Runtime: 845 ms, Memory: 32.3 MB
# Submission Id: 1121431014


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        tmp = []
        for num in nums:
            if not tmp or len(tmp[-1]) == 3 or num - tmp[-1][0] > k:
                tmp.append([])
            tmp[-1].append(num)
            
        for arr in tmp:
            if len(arr) < 3:
                return []
        return tmp