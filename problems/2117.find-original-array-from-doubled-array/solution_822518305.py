# 2117 - Find Original Array From Doubled Array
# Date: 2022-10-15
# Runtime: 3183 ms, Memory: 32.3 MB
# Submission Id: 822518305


from collections import defaultdict

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            return []

        table = defaultdict(int)
        for num in changed:
            table[num] += 1

        ans = []
        for num in sorted(changed):
            if table[num]:
                table[num] -= 1
                if table[num*2] <= 0:
                    return []
                table[num*2] -= 1
                ans.append(num)
        return ans