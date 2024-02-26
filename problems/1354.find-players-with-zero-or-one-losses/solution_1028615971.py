# 1354 - Find Players With Zero or One Losses
# Date: 2023-08-22
# Runtime: 2246 ms, Memory: 73.4 MB
# Submission Id: 1028615971


from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player = set()
        counter = defaultdict(int)
        for winner, loser in matches:
            player.add(winner)
            player.add(loser)
            counter[loser] += 1
        
        win = [p for p in range(1, 100001) if p in player and counter[p] == 0]
        lose = [p for p in range(1, 100001) if p in player and counter[p] == 1]
        return [win, lose]