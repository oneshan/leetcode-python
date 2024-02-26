# 0956 - Number of Music Playlists
# Date: 2023-08-06
# Runtime: 94 ms, Memory: 19.9 MB
# Submission Id: 1013526444


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 1_000_000_007
        
        @cache
        def recur(i, j):
            if i == 0 and j == 0:
                return 1
            if i == 0 or j == 0:
                return 0
            count = recur(i-1, j-1) * (n - j + 1) % mod
            if j > k:
                count += recur(i-1, j) * (j - k) % mod
                count %= mod
            return count
            
                
        return recur(goal, n)