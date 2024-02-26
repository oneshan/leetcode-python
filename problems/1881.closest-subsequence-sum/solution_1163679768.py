# 1881 - Closest Subsequence Sum
# Date: 2024-02-02
# Runtime: 7309 ms, Memory: 179.2 MB
# Submission Id: 1163679768


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        
        def get_subsum(arr):
            n, subset_sums = len(arr), set()
            for mask in range(1 << n):
                s = sum([arr[idx] for idx in range(n) if mask & (1 << idx)])
                subset_sums.add(s)
            return subset_sums
        
        half_n = n >> 1
        left, right = nums[:half_n], nums[half_n:]
        s1 = get_subsum(left)
        s2 = sorted(get_subsum(right))

        ans = 10 ** 10
        for left_sum in s1:
            idx = bisect.bisect_left(s2, goal - left_sum)
            if idx < len(s2):
                arr = left_sum + s2[idx]
                ans = min(ans, abs(goal - arr))
            if idx > 0:
                arr = left_sum + s2[idx-1]
                ans = min(ans, abs(goal - arr))
                
        return ans