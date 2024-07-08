# 3436 - Find Subarray With Bitwise OR Closest to K
# Date: 2024-06-05
# Runtime: 4255 ms, Memory: 28.1 MB
# Submission Id: 1278440605


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        
        curr = ~0
        left = 0
        counter = Counter()

        for right, num in enumerate(nums):
            curr &= num
            for i in range(30):
                if num & (1 << i):
                    counter[i] += 1
            ans = min(ans, abs(k - curr))

            while k > curr:
                for i in range(30):
                    if nums[left] & (1 << i):
                        counter[i] -= 1
                    if counter[i] == right - left:
                        curr |= (1 << i)

                ans = min(ans, abs(k - curr))
                left += 1

        return ans