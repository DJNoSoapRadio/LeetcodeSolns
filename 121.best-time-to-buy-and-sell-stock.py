#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if lowestPrice > price:
                lowestPrice = price
        
            profit = price - lowestPrice
        
            if profit > maxProfit:
                maxProfit = profit
                
        return maxProfit
                
# @lc code=end

