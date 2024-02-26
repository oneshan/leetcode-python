# 2162 - Partition Array Into Two Arrays to Minimize Sum Difference
# Date: 2024-02-02
# Runtime: 942 ms, Memory: 18.2 MB
# Submission Id: 1163662546


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        def get_subsum(arr, k):
            return {sum(comb) for comb in combinations(arr, k)}
        
        half_n = n >> 1
        left, right = nums[:half_n], nums[half_n:]
        total = sum(nums)
        target = total >> 1
        
        ans = abs(sum(left) - sum(right))
        for k in range(1, (half_n >> 1)+1):
            s1 = get_subsum(left, k)
            s2 = sorted(get_subsum(right, half_n-k))            
            for left_sum in s1:
                idx = bisect.bisect_left(s2, target - left_sum)
                if idx < len(s2):
                    arr1 = left_sum + s2[idx]
                    arr2 = total - arr1
                    ans = min(ans, abs(arr1 - arr2))
                if idx > 0:
                    arr1 = left_sum + s2[idx-1]
                    arr2 = total - arr1
                    ans = min(ans, abs(arr1 - arr2))
                
        return ans