# 0912 - Random Pick with Weight
# Date: 2022-10-08
# Runtime: 222 ms, Memory: 18.4 MB
# Submission Id: 817881574


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = self.total * random.random()
        left, right = 0, len(self.prefix_sum)-1
        while left < right:
            mid = left + (right-left) // 2
            if target > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()