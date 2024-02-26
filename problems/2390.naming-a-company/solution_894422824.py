# 2390 - Naming a Company
# Date: 2023-02-09
# Runtime: 540 ms, Memory: 28.5 MB
# Submission Id: 894422824


from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        group = defaultdict(set)
        for idea in ideas:
            group[ord(idea[0]) - ord('a')].add(idea[1:])
        
        ans = 0
        for i in range(25):
            for j in range(i + 1, 26):
                k = len(group[i] & group[j])
                ans += 2 * (len(group[i]) - k) * (len(group[j]) - k)
        return ans        