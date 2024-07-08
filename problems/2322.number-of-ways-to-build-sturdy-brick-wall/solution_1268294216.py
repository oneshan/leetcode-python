# 2322 - Number of Ways to Build Sturdy Brick Wall
# Date: 2024-05-26
# Runtime: 1938 ms, Memory: 16.8 MB
# Submission Id: 1268294216


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

        dp = [0] * (1 << width)
        for mask in masks:
            dp[mask] = 1
            
        for _ in range(1, height):
            next_dp = [0] * (1 << width)
            for mask in masks:
                for prev_mask in masks:
                    if mask & prev_mask:
                        continue
                    next_dp[mask] += dp[prev_mask] % MOD
            dp = next_dp
        
        return sum(dp) % MOD