# 0438 - Find All Anagrams in a String
# Date: 2022-07-21
# Runtime: 203 ms, Memory: 15.2 MB
# Submission Id: 753008478


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table_p = [0] * 26
        table_q = [0] * 26
        for ch in p:
            i_ch = ord(ch) - ord('a')
            table_p[i_ch] += 1
        
        ans = []
        for idx, ch in enumerate(s):
            i_ch = ord(ch) - ord('a')
            table_q[i_ch] += 1
            if idx >= len(p):
                old_ch = ord(s[idx-len(p)]) - ord('a')
                table_q[old_ch] -= 1
            if table_p == table_q:
                ans.append(idx-len(p)+1)

        return ans