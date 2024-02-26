# 0912 - Random Pick with Weight
# Date: 2023-11-02
# Runtime: 173 ms, Memory: 21.2 MB
# Submission Id: 1089901203


class Solution:
    
    def __init__(self, w: List[int]):
        self.prefix_sum = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix_sum.append(curr_sum)
        self.total_sum = curr_sum
        
    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sum)-1
        while left < right:
            mid = (left + right) // 2
            if target <= self.prefix_sum[mid]:
                right = mid
            else:
                left = mid + 1
        return left 