# 0740 - Delete and Earn
# Date: 2024-04-11
# Runtime: 76 ms, Memory: 18.8 MB
# Submission Id: 1229207792


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        arr = sorted(counter.keys())
        if len(arr) == 1:
            return counter[arr[0]] * arr[0]

        dp = [0] * len(arr)
        dp[0] = counter[arr[0]] * arr[0]
                
        if arr[0] + 1 == arr[1]:
            dp[1] = max(dp[0], counter[arr[1]] * arr[1])
        else:
            dp[1] = dp[0] + counter[arr[1]] * arr[1]
            
        for i in range(2, len(arr)):
            if arr[i-1] + 1 == arr[i]:
                dp[i] = max(dp[i-2] + counter[arr[i]] * arr[i], dp[i-1])
            else:
                dp[i] = dp[i-1] + counter[arr[i]] * arr[i]

        return dp[-1]