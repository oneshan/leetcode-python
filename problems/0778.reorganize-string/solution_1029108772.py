# 0778 - Reorganize String
# Date: 2023-08-23
# Runtime: 49 ms, Memory: 16.4 MB
# Submission Id: 1029108772


from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = Counter(s)
        
        max_ch, max_count = '', 0
        for ch, count in counter.items():
            if max_count < count:
                max_ch, max_count = ch, count
        counter.pop(max_ch)
        
        if max_count > (n+1) // 2:
            return ''
        
        ans = [''] * n
        idx = 0
        
        for i in range(max_count):
            ans[idx] = max_ch
            idx += 2
        
        for ch, count in counter.items():
            for i in range(count):
                if idx >= n:
                    idx = 1
                ans[idx] = ch
                idx += 2
        return ''.join(ans)