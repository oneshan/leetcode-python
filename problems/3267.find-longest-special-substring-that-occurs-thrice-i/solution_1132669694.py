# 3267 - Find Longest Special Substring That Occurs Thrice I
# Date: 2023-12-31
# Runtime: 84 ms, Memory: 17.2 MB
# Submission Id: 1132669694


from collections import defaultdict
import heapq

class Solution:
    def maximumLength(self, s: str) -> int:
        table = defaultdict(dict)
        prev, curr = '', 0
        for ch in s:
            if prev != ch:
                table[prev][curr] = table[prev].get(curr, 0) + 1
                prev, curr = ch, 0
            curr += 1
        table[ch][curr] = table[ch].get(curr, 0) + 1
         
        ans = -1
        for counts in table.values():  
            max_len = max(counts)
            if counts[max_len] == 3:
                ans = max(ans, max_len)
            elif counts[max_len] == 2 and max_len > 1:
                ans = max(ans, max_len-1)
            elif counts[max_len] == 1 and counts.get(max_len-1):
                ans = max(ans, max_len-1)
            elif max_len > 2:
                ans = max(ans, max_len-2)
                
        return ans