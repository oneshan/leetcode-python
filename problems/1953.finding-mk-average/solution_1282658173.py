# 1953 - Finding MK Average
# Date: 2024-06-09
# Runtime: 1761 ms, Memory: 53.4 MB
# Submission Id: 1282658173


class BITTree:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * (size + 1)

    def add(self, idx, val):
        idx += 1
        while idx <= self.size:
            self.bits[idx] += val
            idx += idx & -idx
    
    def get_sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bits[idx]
            idx -= idx & -idx
        return res

class MKAverage:

    def __init__(self, m: int, k: int):
        self.value = BITTree(10 ** 5 + 1)
        self.index = BITTree(10 ** 5 + 1)
        self.queue = deque()
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.value.add(num, num)
        self.index.add(num, 1)
        self.queue.append(num)
        if len(self.queue) > self.m:
            num = self.queue.popleft()
            self.value.add(num, -num)
            self.index.add(num, -1)

    def _get_index(self, k):
        left, right = 0, 10 ** 5 + 1
        while left < right:
            mid = (left + right) // 2
            if self.index.get_sum(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1

        left = self._get_index(self.k)
        left_sum = self.value.get_sum(left) - left * (self.index.get_sum(left) - self.k)

        right = self._get_index(self.m-self.k)
        right_sum = self.value.get_sum(right) - right * (self.index.get_sum(right) - (self.m - self.k))
        
        return (right_sum - left_sum) // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()