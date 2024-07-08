# 0903 - Implement Rand10() Using Rand7()
# Date: 2024-05-27
# Runtime: 177 ms, Memory: 19 MB
# Submission Id: 1268947136


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        N, M, randN = 7, 10, rand7
        valid = N * N - (N * N) % M

        while True:
            row = randN() - 1
            col = randN() - 1
            idx = row * N + col
            if idx < valid:
                break

        return 1 + idx % M