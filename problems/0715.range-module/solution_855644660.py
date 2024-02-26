# 0715 - Range Module
# Date: 2022-12-07
# Runtime: 4047 ms, Memory: 32 MB
# Submission Id: 855644660


class Node:
    def __init__(self, lx, rx, cover=False):
        self.s = lx
        self.e = rx
        self.left = None
        self.right = None
        self.cover = cover
    
    
class RangeModule:

    def __init__(self):
        self.root = Node(1, 1_000_000_000)

    def _update(self, node, val, query_s, query_e):
        # Non overlap
        if query_e < node.s or query_s > node.e:
            return
        
        # Full overlap
        if query_s <= node.s and node.e <= query_e:
            node.cover = val
            node.left = node.right = None
            return
        
        # Partial overlap
        if not node.left:
            mid = (node.s + node.e) // 2
            node.left = Node(node.s, mid, node.cover)
            node.right = Node(mid+1, node.e, node.cover)
        self._update(node.left, val, query_s, query_e)
        self._update(node.right, val, query_s, query_e)
        node.cover = node.left.cover and node.right.cover
        
    def addRange(self, left: int, right: int) -> None:
        self._update(self.root, True, left, right-1)

    def queryRange(self, left: int, right: int) -> bool:
        def query(node, query_s, query_e):
            if query_e < node.s or node.e < query_s:
                return True
            if not node.left or (query_s <= node.s and node.e <= query_e):
                return node.cover
            return query(node.left, query_s, query_e) and query(node.right, query_s, query_e)
        return query(self.root, left, right-1)
    
    def removeRange(self, left: int, right: int) -> None:
        self._update(self.root, False, left, right-1)        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)