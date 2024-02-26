# 1354 - Find Players With Zero or One Losses
# Date: 2023-08-22
# Runtime: 2127 ms, Memory: 73.1 MB
# Submission Id: 1028621549


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        counter = [-1] * 100001
        for winner, loser in matches:
            if counter[winner] == -1:
                counter[winner] = 0
            if counter[loser] == -1:
                counter[loser] = 1
            else:
                counter[loser] += 1

        win, lose = [], []
        for i in range(1, 100001):
            if counter[i] == 0:
                win.append(i)
            elif counter[i] == 1:
                lose.append(i)
        return [win, lose]