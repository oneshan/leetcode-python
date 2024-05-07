# 0347 - Top K Frequent Elements
# Date: 2024-05-06
# Runtime: 85 ms, Memory: 27.1 MB
# Submission Id: 1250818483


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        buckets = defaultdict(list)
        for num, freq in counter.items():
            buckets[freq].append(num)

        ans = []
        for i in range(len(nums), -1, -1):
            k -= len(buckets[i])
            ans += buckets[i]
            if k == 0:
                break

        return ans