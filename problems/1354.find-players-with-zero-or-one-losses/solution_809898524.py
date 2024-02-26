# 1354 - Find Players With Zero or One Losses
# Date: 2022-09-27
# Runtime: 4385 ms, Memory: 68.9 MB
# Submission Id: 809898524


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        multi_losers = set()
        losers = set()
        
        for winner, loser in matches:
            if loser in losers:
                multi_losers.add(loser)
            winners.add(winner)
            losers.add(loser)
            
        return [sorted(winners-losers), sorted(losers-multi_losers)]