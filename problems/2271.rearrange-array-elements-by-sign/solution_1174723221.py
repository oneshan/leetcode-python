# 2271 - Rearrange Array Elements by Sign
# Date: 2024-02-14
# Runtime: 999 ms, Memory: 47.1 MB
# Submission Id: 1174723221


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_i, neg_i = 0, 1
        ans = [0] * len(nums)

        for num in nums:
            if num > 0:
                ans[pos_i] = num
                pos_i += 2
            else:
                ans[neg_i] = num
                neg_i += 2
        return ans