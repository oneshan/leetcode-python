# 2550 - Words Within Two Edits of Dictionary
# Date: 2023-09-24
# Runtime: 55 ms, Memory: 16.5 MB
# Submission Id: 1057800917


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        
        for query in queries:
            for word in dictionary:
                diff = 0
                for c1, c2 in zip(query, word):
                    if c1 != c2:
                        diff += 1
                    if diff > 2:
                        break
                else:
                    ans.append(query)
                    break
        return ans