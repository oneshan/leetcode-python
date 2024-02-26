# 2392 - Successful Pairs of Spells and Potions
# Date: 2023-09-17
# Runtime: 1381 ms, Memory: 39.7 MB
# Submission Id: 1051746022


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = [0] * len(spells)
        for idx, spell in enumerate(spells):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1            
            ans[idx] = n - left
        return ans