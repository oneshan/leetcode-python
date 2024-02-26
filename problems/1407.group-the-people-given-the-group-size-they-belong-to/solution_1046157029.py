# 1407 - Group the People Given the Group Size They Belong To
# Date: 2023-09-11
# Runtime: 78 ms, Memory: 16.5 MB
# Submission Id: 1046157029


from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        ans = []
        for idx, size in enumerate(groupSizes):
            groups[size].append(idx)
            if len(groups[size]) == size:
                ans.append(groups.pop(size))
        return ans