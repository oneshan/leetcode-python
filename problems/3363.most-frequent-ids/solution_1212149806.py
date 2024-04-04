# 3363 - Most Frequent IDs
# Date: 2024-03-24
# Runtime: 790 ms, Memory: 41.4 MB
# Submission Id: 1212149806


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = Counter()
        
        max_freq_id = None
        max_freq = float('-inf')
        
        ans = []
        for num, count in zip(nums, freq):
            counter[num] += count
            if count == 0:
                pass
            elif counter[num] > max_freq:
                max_freq_id, max_freq = num, counter[num]
            elif num == max_freq_id:
                max_freq_id, max_freq = counter.most_common(1)[0]
                        
            ans.append(max_freq)
        return ans