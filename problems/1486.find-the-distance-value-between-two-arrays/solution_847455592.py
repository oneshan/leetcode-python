# 1486 - Find the Distance Value Between Two Arrays
# Date: 2022-11-21
# Runtime: 223 ms, Memory: 14 MB
# Submission Id: 847455592


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n = len(arr2)
        arr2.sort()
        
        def get_distance(num):
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] == num:
                    return 0
                if arr2[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return min(num-arr2[right] if right >= 0 else float('inf'),
                       arr2[left]-num if left < n else float('inf'))
        
        return sum(get_distance(num) > d for num in arr1)