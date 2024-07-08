# 2442 - Number of Arithmetic Triplets
# Date: 2024-06-01
# Runtime: 50 ms, Memory: 16.6 MB
# Submission Id: 1273888741


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # nums[j] - nums[i] == nums[k] - nums[j] == diff
        # nums[k] = nums[j] + diff = nums[i] + 2 * diff

        def binary_search(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False


        ans = 0
        n = len(nums)
        for i in range(n-2):
            j = binary_search(i+1, n-1, nums[i]+diff)
            k = binary_search(i+2, n-1, nums[i]+2*diff)
            if j and k:
                ans += 1

        return ans