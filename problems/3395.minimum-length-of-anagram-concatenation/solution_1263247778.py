# 3395 - Minimum Length of Anagram Concatenation
# Date: 2024-05-21
# Runtime: 86 ms, Memory: 17.6 MB
# Submission Id: 1263247778


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
            c1 = Counter()
            for i in range(size):
                c1[s[i]] += 1
            j = size
            while j < n:
                c2 = Counter()
                for _ in range(size):
                    c2[s[j]] += 1
                    j += 1
                if c1 != c2:
                    return False

            return True

        min_size = n // reduce(gcd, counter.values())
        for size in range(min_size, n, min_size):
            if n % size:
                continue
            if check(size):
                return size
        return n
            