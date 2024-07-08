# 1217 - Relative Sort Array
# Date: 2024-06-11
# Runtime: 40 ms, Memory: 16.6 MB
# Submission Id: 1284576704


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)

        ans = []
        for num in arr2:
            ans += [num] * counter[num]
            counter.pop(num)

        for num in sorted(counter):
            ans += [num] * counter[num]
        return ans