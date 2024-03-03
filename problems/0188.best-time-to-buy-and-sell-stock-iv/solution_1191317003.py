# 0188 - Best Time to Buy and Sell Stock IV
# Date: 2024-03-02
# Runtime: 92 ms, Memory: 16.5 MB
# Submission Id: 1191317003


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        arr = [[float('inf'), 0] for _ in range(k)]

        for price in prices:
            arr[0][0] = min(arr[0][0], price)
            arr[0][1] = max(arr[0][1], price - arr[0][0])

            for i in range(1, k):
                arr[i][0] = min(arr[i][0], price - arr[i-1][1])
                arr[i][1] = max(arr[i][1], price - arr[i][0])
        return arr[-1][1]