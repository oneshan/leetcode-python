# 0718 - Maximum Length of Repeated Subarray
# Date: 2024-05-03
# Runtime: 98 ms, Memory: 16.9 MB
# Submission Id: 1248082078


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        BASE = 101
        MOD = 1_000_000_007

        def rolling(nums, size):
            ha, power = 0, 1
            for i in range(size):
                ha = (ha * BASE + nums[i]) % MOD
            for i in range(size-1):
                power = (power * BASE) % MOD

            yield ha, 0
            for i in range(size, len(nums)):
                ha = ((ha - (nums[i-size] * power)) * BASE + nums[i]) % MOD
                yield ha, i-size+1

        def check(size):
            seen = defaultdict(list)
            for ha, start in rolling(nums1, size):
                seen[ha].append(start)
            for ha, start in rolling(nums2, size):
                if ha not in seen:
                    continue
                for i in seen[ha]:
                    if nums1[i: i + size] == nums2[start: start + size]:
                        return True
            return False

        left, right = 1, min(len1, len2) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1