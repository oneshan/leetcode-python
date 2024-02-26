# 2117 - Find Original Array From Doubled Array
# Date: 2023-10-26
# Runtime: 1063 ms, Memory: 34.6 MB
# Submission Id: 1084660519


from collections import Counter
import heapq

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            return []

        counter = Counter(changed)

        zeros = counter.pop(0, 0)
        if zeros & 1:
            return []
        ans = [0] * (zeros >> 1) if zeros else []
        
        for num in sorted(counter):
            counter[num * 2] -= counter[num]
            if counter[num * 2] < 0:
                return []
            ans.extend([num] * counter[num])
        return ans