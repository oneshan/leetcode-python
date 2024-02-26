# 2016 - Reduction Operations to Make the Array Elements Equal
# Date: 2023-11-19
# Runtime: 937 ms, Memory: 30.7 MB
# Submission Id: 1101951551


from collections import Counter

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        arr = [(num, freq) for num, freq in counter.items()]
        arr.sort(reverse=True)
        ans = curr = 0
        for i in range(len(arr)-1):
            curr += arr[i][1]
            ans += curr
        return ans