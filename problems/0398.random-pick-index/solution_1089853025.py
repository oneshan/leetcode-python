# 0398 - Random Pick Index
# Date: 2023-11-02
# Runtime: 320 ms, Memory: 26.1 MB
# Submission Id: 1089853025


class Solution:

    def __init__(self, nums: List[int]):
        self.table = defaultdict(list)
        for idx, num in enumerate(nums):
            self.table[num].append(idx)

    def pick(self, target: int) -> int:
        return choice(self.table[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)