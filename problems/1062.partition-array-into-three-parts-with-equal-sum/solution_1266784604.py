# 1062 - Partition Array Into Three Parts With Equal Sum
# Date: 2024-05-25
# Runtime: 236 ms, Memory: 23.1 MB
# Submission Id: 1266784604


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3

        cnt = curr = 0
        for num in arr:
            curr += num
            if curr == target:
                curr = 0
                cnt += 1
        return cnt >= 3