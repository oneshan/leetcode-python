# 0525 - Contiguous Array
# Date: 2024-03-16
# Runtime: 602 ms, Memory: 22.3 MB
# Submission Id: 1205253098


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = defaultdict(int)
        table[0] = -1

        ans = count = 0
        for idx, num in enumerate(nums):
            count += (1 if num == 0 else -1)
            if count in table:
                ans = max(ans, idx - table[count])
            else:
                table[count] = idx
        return ans