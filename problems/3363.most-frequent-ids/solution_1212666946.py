# 3363 - Most Frequent IDs
# Date: 2024-03-24
# Runtime: 1293 ms, Memory: 44.8 MB
# Submission Id: 1212666946


from sortedcontainers import SortedList
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = Counter()
        sl = SortedList()
        
        ans = []
        for num, count in zip(nums, freq):
            sl.discard(counter[num])
            counter[num] += count
            sl.add(counter[num])
            ans.append(sl[-1])
        return ans