# 0948 - Sort an Array
# Date: 2024-06-12
# Runtime: 1293 ms, Memory: 39.4 MB
# Submission Id: 1285083792


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)

        def merge_sort(left, right):
            if left >= right:
                return
            
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid+1, right)
            merge(left, mid, right)

        def merge(left, mid, right):
            # arr1 = nums[left:mid+1]
            # arr2 = nums[mid+1:right+1]
            
            n1 = mid - left + 1
            n2 = right - mid

            for i in range(left, mid+1):
                temp[i] = nums[i]
            for i in range(mid+1, right+1):
                temp[i] = nums[i]

            p1, p2, k = left, mid+1, left
            while p1 <= mid and p2 <= right:
                if temp[p1] <= temp[p2]:
                    nums[k] = temp[p1]
                    p1 += 1
                else:
                    nums[k] = temp[p2]
                    p2 += 1
                k += 1

            while p1 <= mid:
                nums[k] = temp[p1]
                k += 1
                p1 += 1

            while p2 <= right:
                nums[k] = temp[p2]
                k += 1
                p2 += 1

        merge_sort(0, len(nums)-1)
        return nums