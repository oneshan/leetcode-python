# 3229 - Minimum Cost to Make Array Equalindromic
# Date: 2023-12-17
# Runtime: 418 ms, Memory: 30 MB
# Submission Id: 1121454688


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        def closest_palindrome(num):
            candidates = []
            size = len(str(num))
            mid = (size + 1) // 2
            if size == 1:
                return range(10)
            
            candidates.append(10 ** size + 1)
            candidates.append(10 ** (size-1) - 1)
            
            prefix = int(str(num)[:mid])
            temp = [prefix, prefix+1, prefix-1]
            print(temp)
            for d in temp:
                res = str(d)
                if size & 1:
                    res = res[:-1]
                peep = str(d) + res[::-1]
                candidates.append(int(peep))
            
            return candidates

        
        n = len(nums)
        nums.sort()
        
        ans = float('inf')
        for candidate in closest_palindrome(nums[n//2]):
            min_diff = 0
            for num in nums:
                min_diff += abs(num - candidate)
            ans = min(ans, min_diff)
        return ans