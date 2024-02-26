# 2392 - Successful Pairs of Spells and Potions
# Date: 2023-09-17
# Runtime: 1402 ms, Memory: 39.2 MB
# Submission Id: 1051745504


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for spell in spells:
            
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1            
            ans.append(n - left)
        return ans