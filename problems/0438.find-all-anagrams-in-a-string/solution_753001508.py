# 0438 - Find All Anagrams in a String
# Date: 2022-07-21
# Runtime: 147 ms, Memory: 15.2 MB
# Submission Id: 753001508


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table_p, table_q = {}, {}
        for ch in p:
            table_p[ch] = table_p.get(ch, 0) + 1
        
        ans = []
        left, len_p = -1, len(p)
        for right, ch in enumerate(s):
            if ch not in table_p:
                left, table_q = -1, {}
                continue
            if left == -1:
                left = right
                
            table_q[ch] = table_q.get(ch, 0) + 1
            if table_p[ch] < table_q[ch]:
                while left < right:
                    table_q[s[left]] -= 1
                    left += 1
                    if s[left-1] == ch:
                        break
            
            if right - left + 1 == len_p:
                ans.append(left)

        return ans