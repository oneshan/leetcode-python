# 0377 - Combination Sum IV
# Date: 2023-09-09
# Runtime: 44 ms, Memory: 16.7 MB
# Submission Id: 1044445241


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        @cache
        def recur(remains):
            if remains == 0:
                return 1
            
            ans = 0
            for num in nums:
                if remains < num:
                    break
                ans += recur(remains-num)
            return ans
        
        return recur(target)