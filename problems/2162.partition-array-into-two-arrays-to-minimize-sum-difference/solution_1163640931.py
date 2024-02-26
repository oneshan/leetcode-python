# 2162 - Partition Array Into Two Arrays to Minimize Sum Difference
# Date: 2024-02-02
# Runtime: 1073 ms, Memory: 17.4 MB
# Submission Id: 1163640931


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        half_n = n >> 1
        target = total // 2
        
        ans = float('inf')
        for k in range((half_n >> 1) + 1):
            left_sums = [sum(comb) for comb in combinations(nums[:half_n], k)]
            right_sums = [sum(comb) for comb in combinations(nums[half_n:], half_n-k)]
            right_sums.sort()
            for left_sum in left_sums:
                idx = bisect.bisect_left(right_sums, target - left_sum)
                for pp in {idx, idx-1}:
                    if 0 <= pp < len(right_sums):
                        arr1 = left_sum + right_sums[pp]
                        arr2 = total - arr1
                        ans = min(ans, abs(arr1 - arr2)) 
        return ans