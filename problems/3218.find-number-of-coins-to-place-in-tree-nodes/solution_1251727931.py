# 3218 - Find Number of Coins to Place in Tree Nodes
# Date: 2024-05-07
# Runtime: 1784 ms, Memory: 39.3 MB
# Submission Id: 1251727931


from sortedcontainers import SortedList

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        n = len(cost)
        ans = [1] * n

        def dfs(node, parent):
            min_heap, neg_heap = [cost[node]], []
            if cost[node] < 0:
                neg_heap.append(-cost[node])

            count = 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_count, child_min_heap, child_neg_heap = dfs(neighbor, node)
                count += child_count
                for val in child_min_heap:
                    heapq.heappush(min_heap, val)
                    if len(min_heap) > 3:
                        heapq.heappop(min_heap)
                for val in child_neg_heap:
                    heapq.heappush(neg_heap, val)
                    if len(neg_heap) > 2:
                        heapq.heappop(neg_heap)

            if count < 3:
                res = 1
            else:
                res = min_heap[2] * min_heap[1] * min_heap[0]
                if len(neg_heap) == 2:
                    res = max(res, neg_heap[0] * neg_heap[1] * max(min_heap))
            ans[node] = max(res, 0)

            return count, min_heap, neg_heap


        dfs(0, None)
        return ans