# 3314 - Most Frequent Prime
# Date: 2024-02-18
# Runtime: 123 ms, Memory: 16.7 MB
# Submission Id: 1178461145


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        len_r, len_c = len(mat), len(mat[0])

        @cache
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            for i in range(5, 1 + int(num**0.5), 6):
                if num % i == 0 or num % (i + 2) == 0:
                    return False
            return True
        
        dirs = (0, 1), (0, -1), (1, 0), (1,-1), (1, 1), (-1, 0), (-1, 1), (-1, -1)
        def get_nums(row, col):
            nums = Counter()
            for dr, dc in dirs:
                next_r, next_c = row, col
                num = mat[row][col]
                while True:
                    next_r += dr
                    next_c += dc
                    if not (0 <= next_r < len_r and 0 <= next_c < len_c):
                        break
                    num = num * 10 + mat[next_r][next_c]
                    if is_prime(num) and num > 10:
                        nums[num] += 1
            return nums
                
        freqs = Counter()
        for r in range(len_r):
            for c in range(len_c):
                freqs += get_nums(r, c)
        
        ans, max_freq = -1, 0
        for num, freq in freqs.items():
            if freq > max_freq:
                ans, max_freq = num, freq
            elif freq == max_freq:
                ans = max(ans, num)
        return ans