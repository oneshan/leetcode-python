# 0307 - Range Sum Query - Mutable
# Date: 2022-12-06
# Runtime: 1963 ms, Memory: 31.7 MB
# Submission Id: 855561564


class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.tree = [0] * self.size + nums
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]

    def update(self, index: int, val: int) -> None:
        n = self.size + index
        self.tree[n] = val
        while n > 1:
            self.tree[n>>1] = self.tree[n] + self.tree[n^1]
            n >>= 1

    def sumRange(self, left: int, right: int) -> int:
        m = self.size + left
        n = self.size + right
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)