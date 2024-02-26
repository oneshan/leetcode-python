# 3266 - Find Longest Special Substring That Occurs Thrice II
# Date: 2023-12-31
# Runtime: 283 ms, Memory: 23.8 MB
# Submission Id: 1132711882


from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        table = defaultdict(list)
        prev, length = '', 0
        for idx, ch in enumerate(s):
            if prev != ch:
                if prev:
                    table[prev].append(length)
                prev, length = ch, 0
            length += 1
        table[prev].append(length)

        ans = -1
        for len_list in table.values():
            len_list.sort()
            size = len(len_list)
            
            ans = max(ans, len_list[-1]-2)
            if size > 1:
                ans = max(ans, min(len_list[-1]-1, len_list[-2]))
            if size > 2:
                ans = max(ans, len_list[-3])
                
        return ans if ans else -1