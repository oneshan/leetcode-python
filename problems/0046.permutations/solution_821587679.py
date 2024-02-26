# 0046 - Permutations
# Date: 2022-10-13
# Runtime: 42 ms, Memory: 14.1 MB
# Submission Id: 821587679


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mask, max_mask = 0, (1 << len(nums))-1
        n = len(nums)
        ans = []
        def generate(curr, mask):
            if mask == max_mask:
                ans.append(curr)
                return
            
            for i in range(n):
                if mask & (1 << i):
                    continue
                mask |= (1<<i)
                generate(curr+[nums[i]], mask)
                mask ^= (1<<i)
        
        generate([], 0)
        return ans