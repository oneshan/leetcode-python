# 3219 - Make Lexicographically Smallest Array by Swapping Elements
# Date: 2023-11-26
# Runtime: 1188 ms, Memory: 39.2 MB
# Submission Id: 1106740101


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = [(num, idx) for idx, num in enumerate(nums)]
        arr.sort()
        n = len(nums)
        
        left, right = 0, 1
        while right < n:
            while right < n and arr[right][0] - arr[right-1][0] <= limit:
                right += 1
            temp = sorted(arr[i][1] for i in range(left, right))
            for idx in temp:
                nums[idx] = arr[left][0]
                left += 1
            right += 1

        return nums