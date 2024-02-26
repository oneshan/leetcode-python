# 0807 - Custom Sort String
# Date: 2023-08-31
# Runtime: 35 ms, Memory: 16.4 MB
# Submission Id: 1036099786


from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        
        ans = []
        for ch in order:
            ans.append(ch * counter[ch])
            counter.pop(ch, None)
            
        for ch in counter:
            ans.append(ch * counter[ch])

        return ''.join(ans)