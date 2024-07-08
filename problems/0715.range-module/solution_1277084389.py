# 0715 - Range Module
# Date: 2024-06-04
# Runtime: 3165 ms, Memory: 71.9 MB
# Submission Id: 1277084389


class SegmentTree:
    def __init__(self):
        self.tree = defaultdict(bool)
        self.lazy = defaultdict(bool)
    
    def update(self, query_s, query_e, root_s, root_e, idx, val):
        # no overlap
        if root_e < query_s or root_s > query_e:
            return
        
        # fully overlap
        if query_s <= root_s and root_e <= query_e:
            self.tree[idx] = val
            self.lazy[idx] = val
            return
        
        # partially overlap
        mid = (root_s + root_e) // 2
        self.push_down(idx)
        self.update(query_s, query_e, root_s, mid, 2 * idx, val)
        self.update(query_s, query_e, mid+1, root_e, 2 * idx+1, val)
        self.tree[idx] = self.tree[2 * idx] and self.tree[2 * idx + 1]

    def push_down(self, idx):
        if idx not in self.lazy:
            return
        self.tree[2 * idx] = self.lazy[2 * idx] = self.lazy[idx]
        self.tree[2 * idx + 1] = self.lazy[2 * idx + 1] = self.lazy[idx]
        del self.lazy[idx]

    def query(self, query_s, query_e, root_s, root_e, idx):
        # no overlap
        if root_e < query_s or root_s > query_e:
            return True
        
        # fully overlap
        if query_s <= root_s and root_e <= query_e:
            return self.tree[idx]

        # partially overlap
        self.push_down(idx)
        mid = (root_s + root_e) // 2
        return (
            self.query(query_s, query_e, root_s, mid, 2 * idx)
            and self.query(query_s, query_e, mid+1, root_e, 2 * idx + 1)
        )

class RangeModule:

    def __init__(self):
        self.tree = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        self.tree.update(left, right-1, 0, 10**9, 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.tree.query(left, right-1, 0, 10**9, 1)

    def removeRange(self, left: int, right: int) -> None:
        self.tree.update(left, right-1, 0, 10**9, 1, False)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)