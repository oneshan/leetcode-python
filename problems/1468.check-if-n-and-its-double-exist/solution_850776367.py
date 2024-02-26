# 1468 - Check If N and Its Double Exist
# Date: 2022-11-28
# Runtime: 57 ms, Memory: 13.8 MB
# Submission Id: 850776367


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