# 2285 - Design Bitset
# Date: 2024-05-23
# Runtime: 1609 ms, Memory: 47.2 MB
# Submission Id: 1265492975


class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.num = 0
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.num & (1 << idx):
            return
        self.ones += 1
        self.num |= (1 << idx)

    def unfix(self, idx: int) -> None:
        if self.num & (1 << idx):
            self.ones -= 1
            self.num -= (1 << idx)

    def flip(self) -> None:
        self.ones = self.size - self.ones
        self.num ^= (1 << self.size) - 1

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.ones == 0:
            return '0' * self.size
        if self.ones == self.size:
            return '1' * self.size

        arr = [0] * self.size
        for i in range(self.size):
            arr[i] = '1' if self.num & (1 << i) else '0'
        return ''.join(arr)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()