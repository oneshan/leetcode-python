# 2162 - Partition Array Into Two Arrays to Minimize Sum Difference
# Date: 2024-02-02
# Runtime: 1048 ms, Memory: 17.4 MB
# Submission Id: 1163633165


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        half_n = n >> 1
        target = total // 2
        
        ans = float('inf')
        for k in range((half_n >> 1) + 1):
            left = [sum(comb) for comb in combinations(nums[:half_n], k)]
            right = [sum(comb) for comb in combinations(nums[half_n:], half_n-k)]
            right.sort()
            for x in left:
                r = target - x
                p = bisect.bisect_left(right, r) 
                for pp in {p, p-1}:
                    if 0 <= pp < len(right):
                        left_sum = x + right[pp]
                        right_sum = total - left_sum
                        diff = abs(left_sum - right_sum)
                        ans = min(ans, diff) 
        return ans