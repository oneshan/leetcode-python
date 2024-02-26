# 0862 - Find And Replace in String
# Date: 2023-09-24
# Runtime: 48 ms, Memory: 16.4 MB
# Submission Id: 1057960123


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = list(s)
        
        for idx, source, target in zip(indices, sources, targets):
            if s[idx:idx+len(source)] == source:
                ans[idx] = target
                for j in range(idx+1, idx+len(source)):
                    ans[j] = ''
        
        return ''.join(ans)