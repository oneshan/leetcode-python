# 1288 - Maximum Subarray Sum with One Deletion
# Date: 2022-10-17
# Runtime: 530 ms, Memory: 24.8 MB
# Submission Id: 824504058


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = curr_sum = curr_sum_deleted = -inf
        for num in arr:
            curr_sum_deleted = max(curr_sum_deleted + num, curr_sum)
            curr_sum = max(curr_sum + num, num)
            ans = max(ans, curr_sum_deleted, curr_sum)
        return ans