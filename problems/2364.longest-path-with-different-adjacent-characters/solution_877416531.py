# 2364 - Longest Path With Different Adjacent Characters
# Date: 2023-01-13
# Runtime: 2412 ms, Memory: 164.4 MB
# Submission Id: 877416531


from collections import defaultdict, Counter

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        tree = defaultdict(set)
        for c, p in enumerate(parent):
            tree[p].add(c)
        
        self.ans = 1
        def traverse(node):
            res = 1
            for child in tree[node]:
                length = traverse(child)
                if s[node] == s[child]:
                    continue
                self.ans = max(self.ans, length + res)
                res = max(res, length+1)
            return res
            
        traverse(0)
        return self.ans