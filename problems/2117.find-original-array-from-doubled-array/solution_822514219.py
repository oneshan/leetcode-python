# 2117 - Find Original Array From Doubled Array
# Date: 2022-10-15
# Runtime: 3044 ms, Memory: 31.9 MB
# Submission Id: 822514219


from collections import defaultdict

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        table = defaultdict(int)
        ans = []
        
        for num in changed:
            table[num] += 1
        
        if table[0] & 1:
            return []
        
        if table[0]:
            ans.extend([0] * (table[0] // 2))
        table.pop(0, None)
        
        for num in sorted(table.keys()):
            if table[num] == 0:
                continue
            table[num*2] -= table[num]
            if table[num*2] < 0:
                return []
            ans.extend([num] * table[num])
        return ans