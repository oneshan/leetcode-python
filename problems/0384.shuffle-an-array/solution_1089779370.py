# 0384 - Shuffle an Array
# Date: 2023-11-02
# Runtime: 141 ms, Memory: 20.4 MB
# Submission Id: 1089779370


class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.original = nums[:]
        self.size = len(nums)
        

    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        for i in range(self.size):
            j = random.randrange(i, self.size)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()