# 0862 - Find And Replace in String
# Date: 2024-06-11
# Runtime: 42 ms, Memory: 16.7 MB
# Submission Id: 1284000637


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []

        table = defaultdict(list)
        for idx, source, target in zip(indices, sources, targets):
            table[idx].append((source, target))

        i, n = 0, len(s)
        while i < n:
            if i not in table:
                ans.append(s[i])
                i += 1
                continue

            for source, target in table[i]:
                if s[i:i+len(source)] == source:
                    ans.append(target)
                    i += len(source)
                    break
            else:
                ans.append(s[i])
                i+=1
        
        return ''.join(ans)