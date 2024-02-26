# 2392 - Successful Pairs of Spells and Potions
# Date: 2022-10-11
# Runtime: 1969 ms, Memory: 37.1 MB
# Submission Id: 820090008


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, spell, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if spell * arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        len_s, len_p = len(spells), len(potions)
        potions.sort()
        ans = [len_p] * len_s
        for i in range(len_s):
            ans[i] -= binary_search(potions, spells[i], success-1)
        return ans