# 1332 - Count Vowels Permutation
# Date: 2024-05-02
# Runtime: 356 ms, Memory: 16.8 MB
# Submission Id: 1247249651


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # Each vowel 'a' may only be followed by an 'e'.
        # Each vowel 'e' may only be followed by an 'a' or an 'i'.
        # Each vowel 'i' may not be followed by another 'i'.
        # Each vowel 'o' may only be followed by an 'i' or a 'u'.
        # Each vowel 'u' may only be followed by an 'a'.

        MOD = 1_000_000_007
        
        dp = [1] * 5  # a, e, i, o, u
        for i in range(1, n):
            new_dp = [0] * 5
            new_dp[0] = dp[1]
            new_dp[1] = dp[0] + dp[2]
            new_dp[2] = dp[0] + dp[1] + dp[3] + dp[4]
            new_dp[3] = dp[2] + dp[4]
            new_dp[4] = dp[0]
            
            dp = new_dp
        
        return sum(dp) % MOD