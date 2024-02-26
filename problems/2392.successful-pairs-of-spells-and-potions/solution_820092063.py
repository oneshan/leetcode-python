# 2392 - Successful Pairs of Spells and Potions
# Date: 2022-10-11
# Runtime: 5311 ms, Memory: 37.4 MB
# Submission Id: 820092063


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, spell, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if spell * arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        len_s, len_p = len(spells), len(potions)
        potions.sort()  # O(mlogm)
        ans = [len_p] * len_s
        for i in range(len_s):
            ans[i] -= binary_search(potions, spells[i], success) # O(nlogm)
        return ans