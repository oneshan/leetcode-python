# 0170 - Two Sum III - Data structure design
# Date: 2022-12-05
# Runtime: 1271 ms, Memory: 18.6 MB
# Submission Id: 855004653


from collections import defaultdict

class TwoSum:

    def __init__(self):
        self.table = defaultdict(int)

    def add(self, number: int) -> None:
        self.table[number] += 1

    def find(self, value: int) -> bool:
        for num in self.table:
            if value - num == num:
                if self.table[num] > 1:
                    return True
            elif value - num in self.table:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)