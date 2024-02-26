# 0299 - Bulls and Cows
# Date: 2022-07-22
# Runtime: 60 ms, Memory: 14 MB
# Submission Id: 753723152


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter_s, counter_g = {}, {}
        bulls = cows = 0
        for ch_s, ch_g in zip(secret, guess):
            if ch_s == ch_g:
                bulls += 1
            else:
                counter_s[ch_s] = counter_s.get(ch_s, 0) + 1
                counter_g[ch_g] = counter_g.get(ch_g, 0) + 1
        
        for ch in counter_s:
            cows += min(counter_s[ch], counter_g.get(ch, 0))
        return f'{bulls}A{cows}B'