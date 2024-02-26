# 0649 - Dota2 Senate
# Date: 2023-05-04
# Runtime: 105 ms, Memory: 16.5 MB
# Submission Id: 944231923


from collections import deque, Counter

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        ban = {'D': 0, 'R': 0}
        
        queue = deque(senate)
        while count['R'] and count['D']:
            ch = queue.popleft()
            another = 'R' if ch == 'D' else 'D'
            if ban[ch]:
                ban[ch] -= 1
                count[ch] -= 1
            else:
                ban[another] += 1
                queue.append(ch)
            
        return 'Radiant' if count['R'] else 'Dire'