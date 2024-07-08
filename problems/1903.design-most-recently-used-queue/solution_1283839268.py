# 1903 - Design Most Recently Used Queue
# Date: 2024-06-10
# Runtime: 412 ms, Memory: 17.8 MB
# Submission Id: 1283839268


class BITTree:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * (size+1)
    
    def add(self, idx, val):
        idx += 1
        while idx <= self.size:
            self.bits[idx] += val
            idx += idx & -idx
        
    def sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bits[idx]
            idx -= idx & -idx
        return res


class MRUQueue:

    def __init__(self, n: int):
        self.clock = n
        self.tree = BITTree(n+2000)  # 2000 calls
        self.nums = [0] * (n+2000)

        for i in range(n):
            self.tree.add(i, 1)
            self.nums[i] = i+1

    def _get_index(self, k):
        left, right = 0, self.clock
        while left < right:
            mid = (left + right) // 2
            if self.tree.sum(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def fetch(self, k: int) -> int:
        idx = self._get_index(k)
        self.tree.add(idx, -1)
        self.tree.add(self.clock, 1)
        self.nums[self.clock] = self.nums[idx]
        self.clock += 1
        return self.nums[idx]



# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)