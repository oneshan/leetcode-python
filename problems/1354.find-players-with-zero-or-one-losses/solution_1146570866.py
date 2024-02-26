# 1354 - Find Players With Zero or One Losses
# Date: 2024-01-15
# Runtime: 1693 ms, Memory: 73.9 MB
# Submission Id: 1146570866


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        players = [0] * 100001
        for winner, loser in matches:
            if players[winner] == 0:
                players[winner] = 1
            if players[loser] in (0, 1):
                players[loser] = -1
            elif players[loser] == -1:
                players[loser] = -2
        
        ans = [[], []]
        for i in range(100001):
            if players[i] == 1:
                ans[0].append(i)
            elif players[i] == -1:
                ans[1].append(i)
        return ans