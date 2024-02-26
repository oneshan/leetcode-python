# 3219 - Make Lexicographically Smallest Array by Swapping Elements
# Date: 2023-11-26
# Runtime: 1708 ms, Memory: 52.5 MB
# Submission Id: 1106749035


class UnionFind:
    def __init__(self, n):
        self.size = n
        self.root = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[ry] > self.rank[rx]:
            self.root[rx] = ry
        else:
            self.rank[rx] += 1
            self.root[ry] = rx
        return True

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = [(num, idx) for idx, num in enumerate(nums)]
        arr.sort()
        n = len(nums)
        
        uf = UnionFind(n)
        for i in range(1, n):
            if arr[i][0] - arr[i-1][0] <= limit:
                uf.union(arr[i][1], arr[i-1][1])
                
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(nums[i])
        for gid in groups:
            groups[gid].sort(reverse=True)
            
        ans = []
        for i in range(n):
            ans.append(groups[uf.find(i)].pop())
        return ans