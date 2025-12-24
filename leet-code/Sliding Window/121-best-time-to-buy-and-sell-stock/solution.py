class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maxProfit_BruteForce(self, prices: list[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n):
            buy = prices[i]
            for j in range(i + 1, n):
                sell = prices[j]
                res = max(res, sell - buy)
        return res 
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit_DynamicProgramming(self, prices: list[int]) -> int:
        res = 0
        n = len(prices)
        min_price = float('inf')
        for i in range(n):
            min_price = min(min_price, prices[i])
            res = max(res, prices[i] - min_price)

        return res
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit_SlidingWindow(self, prices: list[int]) -> int:
        res = 0
        buy = 0
        sell = 1
        n = len(prices)
        while sell < n:
            if prices[buy] < prices[sell]:
                res = max(res, prices[sell] - prices[buy])
            else:
                buy = sell

            sell += 1
        return res
            