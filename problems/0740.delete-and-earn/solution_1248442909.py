# 0740 - Delete and Earn
# Date: 2024-05-03
# Runtime: 80 ms, Memory: 28 MB
# Submission Id: 1248442909


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += num

        max_num = max(counter)

        @cache
        def dp(i):
            if i >= max_num:
                return 0
            return max(dp(i+1), counter[i+1] + dp(i+2))

        return dp(0)