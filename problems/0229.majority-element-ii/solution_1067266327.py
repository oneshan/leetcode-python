# 0229 - Majority Element II
# Date: 2023-10-05
# Runtime: 125 ms, Memory: 17.8 MB
# Submission Id: 1067266327


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
                
        target_count = len(nums) / 3    
        c1 = c2 = 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
                
        ans = []
        if c1 > target_count:
            ans.append(n1)
        if c2 > target_count:
            ans.append(n2)
        return ans