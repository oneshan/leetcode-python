# 0874 - Backspace String Compare
# Date: 2023-10-19
# Runtime: 38 ms, Memory: 16.1 MB
# Submission Id: 1079014276


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ps, pt = len(s)-1, len(t)-1
        while ps >= 0 or pt >= 0:
            skip = 0  
            while ps >= 0:
                if s[ps] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    break
                ps -= 1
                
            skip = 0  
            while pt >= 0:
                if t[pt] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    break
                pt -= 1
            
            if ps >= 0 and pt >= 0 and s[ps] != t[pt]:
                return False
            
            if (ps >= 0) != (pt >= 0):
                return False
            
            ps -= 1
            pt -= 1
        
        return True