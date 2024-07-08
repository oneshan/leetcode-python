# 2696 - The Number of Beautiful Subsets
# Date: 2024-05-23
# Runtime: 54 ms, Memory: 16.6 MB
# Submission Id: 1265362304


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        buckets = defaultdict(set)
        for num in nums:
            buckets[num % k].add(num)
        
        prev = -k
        skip = pick = 0
        for subset in buckets.values():
            for num in sorted(subset):
                cnt = (1 << counter[num]) - 1
                skip, pick = skip + pick, cnt * (1 + skip + (0 if num-prev == k else pick))
                prev = num
                
        return skip + pick