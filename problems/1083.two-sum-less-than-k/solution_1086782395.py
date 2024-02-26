# 1083 - Two Sum Less Than K
# Date: 2023-10-29
# Runtime: 64 ms, Memory: 16.1 MB
# Submission Id: 1086782395


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        ans = -1
        counter = Counter(nums)
        
        left, right = 1, 1001
        while left <= right:
            if counter[right] == 0 or left + right >= k:
                right -= 1
            else:
                if counter[left] > (0 if left < right else 1):
                    ans = max(ans, left + right)
                left += 1
        return ans