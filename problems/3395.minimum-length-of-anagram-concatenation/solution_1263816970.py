# 3395 - Minimum Length of Anagram Concatenation
# Date: 2024-05-21
# Runtime: 92 ms, Memory: 17.5 MB
# Submission Id: 1263816970


class Solution:
    def minAnagramLength(self, s: str) -> int:
        
        n = len(s)
        counter = Counter(s)
        if len(counter) == 1:
            return 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def check(size):
            prev = None
            for i in range(0, n, size):
                curr = Counter()
                for j in range(size):
                    curr[s[i+j]] += 1
                if prev and prev != curr:
                    return False
                prev = curr
            return True

        min_size = n // reduce(gcd, counter.values())
        for size in range(min_size, n, min_size):
            if n % size:
                continue
            if check(size):
                return size
        return n
            