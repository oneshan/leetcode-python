# 0229 - Majority Element II
# Date: 2023-07-22
# Runtime: 136 ms, Memory: 17.9 MB
# Submission Id: 1000688539


from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target_count = len(nums) / 3
        
        count1, count2, major1, major2 = 0, 0, None, None
        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
            elif count1 == 0:
                major1, count1 = num, 1
            elif count2 == 0:
                major2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        count1 = count2 = 0
        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
                
        ans = []
        if count1 > target_count:
            ans.append(major1)
        if count2 > target_count:
            ans.append(major2)
        
        
        return ans