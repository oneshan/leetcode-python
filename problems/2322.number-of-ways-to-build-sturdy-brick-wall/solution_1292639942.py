# 2322 - Number of Ways to Build Sturdy Brick Wall
# Date: 2024-06-19
# Runtime: 2667 ms, Memory: 17.1 MB
# Submission Id: 1292639942


class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        MOD = 1_000_000_007
        masks = []

        @cache
        def get_all_masks(mask, curr_width):
            for brick in bricks:
                next_width = curr_width + brick
                if next_width > width:
                    continue
                if next_width == width:
                    masks.append(mask)
                    continue
                next_mask = mask | (1 << next_width)
                get_all_masks(next_mask, next_width)

        get_all_masks(0, 0)

        dp = [1] * len(masks)
        n = len(masks)

        for _ in range(1, height):
            next_dp = [0] * len(masks)
            for i in range(n):
                for j in range(n):
                    if masks[i] & masks[j]:
                        continue
                    next_dp[j] += dp[i] % MOD
            dp = next_dp
        
        return sum(dp) % MOD