# 0742 - To Lower Case
# Date: 2022-11-17
# Runtime: 64 ms, Memory: 13.8 MB
# Submission Id: 844902572


class Solution:
    def toLowerCase(self, s: str) -> str:
        lower_case = ord('a')
        upper_case = ord('A')
        delta = lower_case - upper_case
        
        list_s = list(s)
        for i in range(len(s)):
            if upper_case <= ord(s[i]) <= upper_case+25:
                list_s[i] = chr(ord(s[i])+delta)
        return ''.join(list_s)