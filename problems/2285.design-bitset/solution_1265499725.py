# 2285 - Design Bitset
# Date: 2024-05-23
# Runtime: 470 ms, Memory: 48.4 MB
# Submission Id: 1265499725


"""
is_flip  bits
True    0   --- 1
True    1   --- 0
False   0   --- 0
False   1   --- 1
"""
class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.is_flip = 0
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.is_flip:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones += 1
        else:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.is_flip:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones -= 1
        else:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones -= 1

    def flip(self) -> None:
        self.is_flip ^= 1
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(str(self.is_flip ^ self.bits[i]) for i in range(self.size))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()