# 3350 - Distribute Elements Into Two Arrays II
# Date: 2024-03-03
# Runtime: 2156 ms, Memory: 34.6 MB
# Submission Id: 1192210093


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = [nums[0]]
        sorted_arr1 = [nums[0]]
        arr2 = [nums[1]]
        sorted_arr2 = [nums[1]]
        
        for i in range(2, n):
            c1 = len(arr1) - bisect.bisect_right(sorted_arr1, nums[i])
            c2 = len(arr2) - bisect.bisect_right(sorted_arr2, nums[i])
            if c1 > c2:
                arr1.append(nums[i])
                bisect.insort_left(sorted_arr1, nums[i])
            elif c1 < c2:
                arr2.append(nums[i])
                bisect.insort_left(sorted_arr2, nums[i])
            elif len(arr1) > len(arr2):
                arr2.append(nums[i])
                bisect.insort_left(sorted_arr2, nums[i])
            else:
                arr1.append(nums[i])
                bisect.insort_left(sorted_arr1, nums[i])
            
        return arr1 + arr2