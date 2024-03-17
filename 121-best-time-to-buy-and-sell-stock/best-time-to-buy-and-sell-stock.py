class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = i = j = 0
        while j < len(prices):
            if prices[j] > prices[i]:
                maxp = max(maxp, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return maxp
        