# 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
# Date: 2023-11-02
# Runtime: 329 ms, Memory: 68.3 MB
# Submission Id: 1089851046


from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.table = defaultdict(set)
        self.arr = []
        self.size = 0
        

    def insert(self, val: int) -> bool:
        self.arr.append(val)
        self.table[val].add(self.size)
        self.size += 1       
        return len(self.table[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.table[val]:
            return False
        
        last_element = self.arr[-1]
        idx = self.table[val].pop()
        
        self.arr[idx] = last_element
        self.table[last_element].add(idx)    
        self.table[last_element].discard(self.size - 1)
        self.arr.pop()
        self.size -= 1
        
        return True
        

    def getRandom(self) -> int:
        return choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()