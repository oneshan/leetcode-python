# 0093 - Restore IP Addresses
# Date: 2023-01-21
# Runtime: 42 ms, Memory: 14 MB
# Submission Id: 882341792


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        ans = []
        
        def backtrack(idx, dots):
            if len(dots) == 4 and idx == len(s):
                ans.append('.'.join(dots))
                return
            if len(dots) > 4:
                return
            for i in range(idx, idx+3):
                if i == len(s) or (i > idx and s[idx] == '0'):
                    break
                if int(s[idx: i+1]) < 256:
                    dots.append(s[idx: i+1])
                    backtrack(i+1, dots)
                    dots.pop()
                    
        backtrack(0, [])
        return ans