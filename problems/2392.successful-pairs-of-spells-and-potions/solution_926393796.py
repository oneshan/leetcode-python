# 2392 - Successful Pairs of Spells and Potions
# Date: 2023-04-02
# Runtime: 1893 ms, Memory: 36.9 MB
# Submission Id: 926393796


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        len_s, len_p = len(spells), len(potions)
        potions.sort()
        ans = [0] * len_s

        def binary_search(spell, target):
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        return [len_p - binary_search(spell, success-1) for spell in spells]