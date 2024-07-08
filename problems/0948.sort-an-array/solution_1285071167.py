# 0948 - Sort an Array
# Date: 2024-06-12
# Runtime: 1486 ms, Memory: 32.6 MB
# Submission Id: 1285071167


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def max_heapify(heap_size, index):
            left = 2 * index + 1
            right = 2 * index + 2
            
            largest = index
            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
                
            if largest != index:
                nums[index], nums[largest] = nums[largest], nums[index]
                max_heapify(heap_size, largest)

        def heap_sort():
            n = len(nums)

            # build head (top-down)
            for i in range(n//2 -1, -1, -1):
                max_heapify(n, i)

            for i in range(n - 1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                max_heapify(i, 0)
        
        heap_sort()
        return nums