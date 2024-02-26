# 0599 - Minimum Index Sum of Two Lists
# Date: 2022-07-17
# Runtime: 206 ms, Memory: 14.5 MB
# Submission Id: 748911233


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        table = {}
        for idx, rest in enumerate(list1):
            table[rest] = idx
            
        ans, ans_sum = [], float('inf')
        for idx, rest in enumerate(list2):
            if rest not in table:
                continue
            curr_sum = idx + table[rest]
            if curr_sum < ans_sum:
                ans, ans_sum = [rest], curr_sum
            elif curr_sum == ans_sum:
                ans.append(rest)
        return ans