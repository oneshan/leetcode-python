# 3350 - Distribute Elements Into Two Arrays II
# Date: 2024-03-03
# Runtime: 1346 ms, Memory: 35.8 MB
# Submission Id: 1192377903


from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = [nums[0]]
        sorted_arr1 = SortedList([nums[0]])
        arr2 = [nums[1]]
        sorted_arr2 = SortedList([nums[1]])
        
        for i in range(2, n):
            c1 = len(arr1) - sorted_arr1.bisect_right(nums[i])
            c2 = len(arr2) - sorted_arr2.bisect_right(nums[i])
            if c1 > c2:
                arr1.append(nums[i])
                sorted_arr1.add(nums[i])
            elif c1 < c2:
                arr2.append(nums[i])
                sorted_arr2.add(nums[i])
            elif len(arr1) > len(arr2):
                arr2.append(nums[i])
                sorted_arr2.add(nums[i])
            else:
                arr1.append(nums[i])
                sorted_arr1.add(nums[i])
            
        return arr1 + arr2