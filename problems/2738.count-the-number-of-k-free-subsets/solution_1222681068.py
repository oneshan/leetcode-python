# 2738 - Count the Number of K-Free Subsets
# Date: 2024-04-04
# Runtime: 54 ms, Memory: 16.7 MB
# Submission Id: 1222681068


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        table = defaultdict(list)
        for num in sorted(nums):
            table[num % k].append(num)

        ans = 1
        for arr in table.values():
            take = notake = 1
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] == k:
                    take, notake = notake, take+notake
                else:
                    take = notake = take + notake
            ans *= (take + notake)

        return ans