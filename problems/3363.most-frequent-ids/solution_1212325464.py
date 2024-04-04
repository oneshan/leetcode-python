# 3363 - Most Frequent IDs
# Date: 2024-03-24
# Runtime: 983 ms, Memory: 48.2 MB
# Submission Id: 1212325464


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = Counter()
        heap = []
        
        ans = []
        for num, count in zip(nums, freq):
            counter[num] += count
            while heap and counter[heap[0][1]] + heap[0][0] != 0:
                heapq.heappop(heap)
            heapq.heappush(heap, (-counter[num], num))
            ans.append(-heap[0][0])
        return ans