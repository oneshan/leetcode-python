# 0686 - Repeated String Match
# Date: 2023-10-28
# Runtime: 342 ms, Memory: 16.7 MB
# Submission Id: 1085870753


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        num_a = [ord(ch) - ord('a') + 1 for ch in a]
        num_b = [ord(ch) - ord('a') + 1 for ch in b]
        len_a, len_b = len(a), len(b)
        
        hash_a = hash_b = 0
        for i in range(len_b):
            hash_b = 26 * hash_b + num_b[i]
            
        aL = 26 ** len_b
        for i in range((len_b // len_a + 2) * len_a):
            hash_a = 26 * hash_a + num_a[i % len_a]
            if i >= len_b:
                hash_a -= num_a[(i-len_b) % len_a] * aL
            if hash_a == hash_b:
                return ceil((i+1) / len_a)
        return -1