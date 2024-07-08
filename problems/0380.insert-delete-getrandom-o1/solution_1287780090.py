# 0380 - Insert Delete GetRandom O(1)
# Date: 2024-06-14
# Runtime: 253 ms, Memory: 63.3 MB
# Submission Id: 1287780090


class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.arr = []
        self.idx = 0

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False

        self.arr.append(val)
        self.table[val] = self.idx
        self.idx += 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False

        idx = self.table[val]
        # move last_element to idx
        last_element = self.arr[-1]
        self.table[last_element] = idx
        self.arr[idx] = last_element

        # delete
        self.arr.pop()
        self.table.pop(val)

        self.idx -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()