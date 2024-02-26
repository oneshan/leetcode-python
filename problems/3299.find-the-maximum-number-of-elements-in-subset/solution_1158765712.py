# 3299 - Find the Maximum Number of Elements in Subset
# Date: 2024-01-28
# Runtime: 1004 ms, Memory: 30.1 MB
# Submission Id: 1158765712


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        ans = max(1, counter[1] - (counter[1] & 1 == 0))
        for num in range(1, 10001):
            if num not in counter:
                continue
            if counter[num] == 1:
                continue
            count = -1
            curr = num
            while curr in counter:
                count += 2
                if counter[curr] == 1:
                    break
                counter.pop(curr)
                curr *= curr
            ans = max(count, ans)
        return ans