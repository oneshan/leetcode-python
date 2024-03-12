# 3356 - Shortest Uncommon Substring in an Array
# Date: 2024-03-10
# Runtime: 231 ms, Memory: 19.5 MB
# Submission Id: 1199248171


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        table = defaultdict(set)
        for i, word in enumerate(arr):
            for j in range(len(word)):
                for k in range(j+1, len(word)+1):
                    sub = word[j:k]
                    table[sub].add(i)

        ans = []
        for i, word in enumerate(arr):
            shorest_sub = ''
            for j in range(len(word)):
                for k in range(j+1, len(word)+1):
                    sub = word[j:k]
                    if sub in table and len(table[sub]) > 1:
                        continue
                    if (not shorest_sub
                        or len(sub) < len(shorest_sub)
                        or (len(sub) == len(shorest_sub) and sub < shorest_sub)
                    ):
                        shorest_sub = sub
            ans.append(shorest_sub)
        return ans