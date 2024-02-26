# 0502 - IPO
# Date: 2022-10-10
# Runtime: 3951 ms, Memory: 36.2 MB
# Submission Id: 819199427


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(sorted(profits, reverse=True)[:k])
        
        projects = sorted(zip(capital, profits))
        n = len(projects)
        for i in range(min(n, k)):
            for j in range(i+1, n):
                if w >= projects[j][0] and projects[j][1] > projects[i][1]:
                    projects[i], projects[j] = projects[j], projects[i]
            if projects[i][0] > w:
                break
            w += projects[i][1]
        return w