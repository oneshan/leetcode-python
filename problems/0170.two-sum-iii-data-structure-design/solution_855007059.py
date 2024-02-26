# 0170 - Two Sum III - Data structure design
# Date: 2022-12-05
# Runtime: 536 ms, Memory: 18.3 MB
# Submission Id: 855007059


class TwoSum:

    def __init__(self):
        self.arr = []
        self.size = 0
        self.is_sorted = True

    def add(self, number: int) -> None:
        self.arr.append(number)
        self.size += 1
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.arr.sort()
            self.is_sorted = True
        
        left, right = 0, self.size-1
        while left < right:
            curr_sum = self.arr[left] + self.arr[right] 
            if curr_sum == value:
                return True
            if curr_sum < value:
                left += 1
            else:
                right -= 1
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)