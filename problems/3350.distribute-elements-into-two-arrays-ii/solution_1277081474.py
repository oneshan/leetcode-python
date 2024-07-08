# 3350 - Distribute Elements Into Two Arrays II
# Date: 2024-06-04
# Runtime: 1399 ms, Memory: 44 MB
# Submission Id: 1277081474


class BITTree:
    def __init__(self, nums):
        self.size = len(nums)
        self.tree = [0] * (self.size + 1)

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx
    
    def get_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ranks = {val: idx for idx, val in enumerate(sorted(set(nums)), 1)}
        arr = [0] * len(ranks)

        bit1 = BITTree(arr)
        bit2 = BITTree(arr)

        arr1 = [nums[0]]
        bit1.update(ranks[nums[0]], 1)
        arr2 = [nums[1]]
        bit2.update(ranks[nums[1]], 1)
        
        for i in range(2, n):
            c1 = len(arr1) - bit1.get_sum(ranks[nums[i]])
            c2 = len(arr2) - bit2.get_sum(ranks[nums[i]])
            if c1 > c2:
                arr1.append(nums[i])
                bit1.update(ranks[nums[i]], 1)
            elif c1 < c2:
                arr2.append(nums[i])
                bit2.update(ranks[nums[i]], 1)
            elif len(arr1) > len(arr2):
                arr2.append(nums[i])
                bit2.update(ranks[nums[i]], 1)
            else:
                arr1.append(nums[i])
                bit1.update(ranks[nums[i]], 1)
            
        return arr1 + arr2