# 2724 - Convert an Array Into a 2D Array With Conditions
# Date: 2024-01-02
# Runtime: 75 ms, Memory: 17.3 MB
# Submission Id: 1134344221


from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        
        ans = []
        for num in nums:
            counter[num] += 1
            if counter[num] > len(ans):
                ans.append([])
            ans[counter[num]-1].append(num)
        return ans