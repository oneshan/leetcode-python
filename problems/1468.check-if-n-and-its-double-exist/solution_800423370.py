# 1468 - Check If N and Its Double Exist
# Date: 2022-09-15
# Runtime: 76 ms, Memory: 14 MB
# Submission Id: 800423370


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num & 1 == 0 and num // 2 in seen:
                return True
            if num * 2 in seen:
                return True
            seen.add(num)
        return False