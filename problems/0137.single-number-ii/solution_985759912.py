# 0137 - Single Number II
# Date: 2023-07-04
# Runtime: 69 ms, Memory: 19.1 MB
# Submission Id: 985759912


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = set()
        two = set()
        for num in nums:
            if num in one:
                two.add(num)
            one.add(num)
            
        return list(one - two)[0]