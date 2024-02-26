# 1332 - Count Vowels Permutation
# Date: 2023-10-28
# Runtime: 540 ms, Memory: 56.6 MB
# Submission Id: 1085865496


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1_000_000_007
        
        mapping = {
            '': set('aeiou'),
            'a': set('e'),
            'e': set('ai'),
            'i': set('aeou'),
            'o': set('iu'),
            'u': set('a')
        }
        
        @cache
        def recur(i, ch):
            if i == n:
                return 1
            count = 0
            for next_ch in mapping[ch]:
                count += recur(i+1, next_ch)
            return count % MOD
        
        return recur(0, '')