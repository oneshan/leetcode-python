# 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
# Date: 2024-06-14
# Runtime: 277 ms, Memory: 68.3 MB
# Submission Id: 1287790585


class RandomizedCollection:

    def __init__(self):
        self.table = defaultdict(set)
        self.arr = []
        self.idx = 0

    def insert(self, val: int) -> bool:
        self.table[val].add(self.idx)
        self.arr.append(val)
        self.idx += 1
        return len(self.table[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.table[val]:
            return False
                    
        idx = self.table[val].pop()
        last_element = self.arr[-1]

        self.arr[idx] = last_element
        self.table[last_element].add(idx)

        self.table[last_element].discard(self.idx-1)
        self.arr.pop()
        self.idx -= 1
        return True

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()