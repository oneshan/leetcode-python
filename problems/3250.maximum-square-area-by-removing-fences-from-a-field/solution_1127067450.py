# 3250 - Maximum Square Area by Removing Fences From a Field
# Date: 2023-12-24
# Runtime: 1517 ms, Memory: 38.1 MB
# Submission Id: 1127067450


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 1_000_000_007
        
        hFences.sort()
        len_h = len(hFences)
        candidates = {m-1}
        for i in range(len_h):
            for j in range(i):
                candidates.add(hFences[i] - hFences[j])
        for fence in hFences:
            candidates.add(fence-1)
            candidates.add(m-fence)
            
        ans = -1
        if (n-1) in candidates:
            ans = max(ans, n-1)

        vFences.sort()
        len_v = len(vFences)
        for i in range(len_v):
            for j in range(i):
                if vFences[i] - vFences[j] in candidates:
                    ans = max(ans, vFences[i] - vFences[j])

        for fence in vFences:
            if fence - 1 in candidates:
                ans = max(ans, fence-1)
            if n - fence in candidates:
                ans = max(ans, n-fence)

        return -1 if ans == -1 else ans ** 2 % MOD