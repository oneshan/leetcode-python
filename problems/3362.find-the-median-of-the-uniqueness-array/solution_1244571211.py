# 3362 - Find the Median of the Uniqueness Array
# Date: 2024-04-29
# Runtime: 4206 ms, Memory: 35.7 MB
# Submission Id: 1244571211


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        target = n * (n+1) // 2

        def check(median):
            counter = Counter()
            res = left = 0
            for right in range(n):
                counter[nums[right]] += 1
                while len(counter) > median:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        counter.pop(nums[left])
                    left += 1
                res += (right - left + 1)
            return 2 * res >= target

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left