# 2915 - Count of Interesting Subarrays
# Date: 2023-09-03
# Runtime: 852 ms, Memory: 45.1 MB
# Submission Id: 1039077713



class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        nums = [int(num % modulo == k) for num in nums]
        counter = defaultdict(int)
        counter[0] = 1
        curr_sum = ans = 0
        for num in nums:
            curr_sum += num
            val = (curr_sum % modulo)
            ans += counter[(val-k) % modulo]
            counter[val] += 1
        return ans