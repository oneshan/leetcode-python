# 1983 - Maximum Population Year
# Date: 2023-09-22
# Runtime: 55 ms, Memory: 16.2 MB
# Submission Id: 1056391568


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        count = [0] * 101
        for birth, death in logs:
            count[birth-1950] += 1
            count[death-1950] -= 1
        
        ans = curr_count = max_count = 0
        for i in range(101):
            curr_count += count[i]
            if curr_count > max_count:
                ans, max_count = 1950 + i, curr_count
        return ans