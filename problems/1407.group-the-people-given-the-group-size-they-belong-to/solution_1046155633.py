# 1407 - Group the People Given the Group Size They Belong To
# Date: 2023-09-11
# Runtime: 64 ms, Memory: 16.4 MB
# Submission Id: 1046155633


from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for idx, size in enumerate(groupSizes):
            groups[size].append(idx)
            
        ans = []
        for size, ids in groups.items():
            for i in range(0, len(ids), size):
                ans.append(ids[i:i+size])
        return ans