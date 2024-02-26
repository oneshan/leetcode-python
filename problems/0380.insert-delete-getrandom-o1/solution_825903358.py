# 0380 - Insert Delete GetRandom O(1)
# Date: 2022-10-19
# Runtime: 972 ms, Memory: 61.7 MB
# Submission Id: 825903358


from random import choice

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.table = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False
        self.arr.append(val)
        self.table[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False
        last_element = self.arr[-1]
        idx = self.table[val]
        
        self.arr[idx] = last_element
        self.table[last_element] = idx
        self.arr.pop()
        self.table.pop(val)
        self.size -= 1
        return True

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()