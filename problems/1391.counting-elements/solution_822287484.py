# 1391 - Counting Elements
# Date: 2022-10-14
# Runtime: 80 ms, Memory: 14.1 MB
# Submission Id: 822287484


from collections import defaultdict
class Solution:
    def countElements(self, arr: List[int]) -> int:
        table = defaultdict(int)
        for num in arr:
            table[num] += 1

        ans = 0
        for num in table:
            ans += table.get(num-1, 0)
        return ans