# 0307 - Range Sum Query - Mutable
# Date: 2022-12-06
# Runtime: 2253 ms, Memory: 31.5 MB
# Submission Id: 855584653


class SegmentTree:
	def __init__(self, nums):
		self.size = len(nums)
		self.tree = [0] * self.size + nums
		for i in range(self.size-1, 0, -1):
			self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
	
	def update(self, i, val):
		n = self.size + i
		self.tree[n] = val
		while n > 1:
			self.tree[n>>1] = self.tree[n] + self.tree[n^1]
			n >>= 1
		
	def sum_range(self, i, j):
		m = self.size + i
		n = self.size + j
		res = 0
		while m <= n:
			if m & 1:  # sum if m is not right child of its parent
				res += self.tree[m]
				m += 1
			m >>= 1
			if n & 1 == 0:  # sum if n is not left child of its parent
				res += self.tree[n]
				n -= 1
			n >>= 1
		return res
    
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sum_range(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)